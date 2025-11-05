// Frontend mínimo para registro y login
// Usamos la API en el mismo dominio
const API_BASE = '';

function el(id){return document.getElementById(id)}

async function postJson(path, data){
  const res = await fetch(API_BASE + path, {
    method: 'POST',
    headers: {'Content-Type':'application/json'},
    body: JSON.stringify(data)
  });
  const json = await res.json().catch(()=>({}));
  return {ok: res.ok, status: res.status, body: json};
}

function showToast(msg){
  let t = document.querySelector('.toast');
  if(!t){
    t = document.createElement('div');
    t.className = 'toast';
    document.body.appendChild(t);
  }
  t.textContent = msg;
  t.classList.add('show');
  setTimeout(()=> t.classList.remove('show'), 3500);
}

function decodeJwt(token){
  try{
    const payload = token.split('.')[1];
    const json = atob(payload.replace(/-/g,'+').replace(/_/g,'/'));
    return JSON.parse(decodeURIComponent(escape(json)));
  }catch(e){return null}
}

// Registro
el('register-form').addEventListener('submit', async (e)=>{
  e.preventDefault();
  const f = new FormData(e.target);
  const username = f.get('username').trim();
  const password = f.get('password');
  const out = el('register-result');
  // Validaciones básicas
  if(username.length < 3){ out.textContent = 'El usuario debe tener al menos 3 caracteres'; out.className='result err'; return; }
  if(password.length < 8){ out.textContent = 'La contraseña debe tener al menos 8 caracteres'; out.className='result err'; return; }
  if(!/[0-9]/.test(password) || !/[!@#$%^&*(),.?":{}|<>]/.test(password)){
    out.textContent = 'La contraseña debe incluir al menos un número y un carácter especial'; out.className='result err'; return;
  }
  out.textContent = '';
  out.className='result';
  const btn = e.target.querySelector('button[type=submit]');
  btn.disabled = true;
  btn.innerHTML = '<span class="loader"></span> Registrando...';

  try{
    const r = await postJson('/registry', {username, password});
    if(r.ok){
      out.textContent = `Usuario creado: ${r.body.username} (id ${r.body.id})`;
      out.classList.add('ok');
      e.target.reset();
      showToast('Registro exitoso. Puedes iniciar sesión.');
    }else{
      out.textContent = r.body.error || `Error ${r.status}`;
      out.classList.add('err');
      showToast(out.textContent);
    }
  }catch(err){
    out.textContent = 'Error de conexión';
    out.classList.add('err');
  }
  btn.disabled = false;
  btn.innerHTML = 'Registrar';
});

// Login
el('login-form').addEventListener('submit', async (e)=>{
  e.preventDefault();
  const f = new FormData(e.target);
  const username = f.get('username');
  const password = f.get('password');
  const out = el('login-result');
  out.textContent = '';
  out.className='result';
  const btn = e.target.querySelector('button[type=submit]');
  btn.disabled = true;
  btn.innerHTML = '<span class="loader"></span> Autenticando...';

  try{
    const r = await postJson('/login', {username, password});
    if(r.ok && r.body.access_token){
      localStorage.setItem('access_token', r.body.access_token);
      out.textContent = 'Login correcto. Token guardado en localStorage.';
      out.classList.add('ok');
      e.target.reset();
      showToast('Login correcto');
      // mostrar panel de cuenta
      const token = r.body.access_token;
      const info = decodeJwt(token) || {};
      const acctId = info.sub || info.user_id || info.identity || info.id || '';
      const acctUsername = info.username || username || '';
      const acctCard = document.getElementById('account-card');
      if(acctCard){ acctCard.classList.remove('hidden'); }
      const acctIdEl = document.getElementById('acct-id');
      const acctUserEl = document.getElementById('acct-username');
      if(acctIdEl) acctIdEl.textContent = acctId;
      if(acctUserEl) acctUserEl.textContent = acctUsername;
      // opcional: traer datos reales desde /users y buscar el id
      if(token){
        try{
          const usersRes = await fetch(API_BASE + '/users', { headers: { 'Authorization': 'Bearer ' + token } });
          if(usersRes.ok){
            const users = await usersRes.json();
            const me = users.find(u => String(u.id) === String(acctId) || String(u.username) === String(acctUsername));
            if(me){
              if(acctIdEl) acctIdEl.textContent = me.id;
              if(acctUserEl) acctUserEl.textContent = me.username;
            }
          }
        }catch(e){/* ignore */}
      }
    }else{
      // Si no autorizado o usuario no existe, sugerir registrarse
      const errMsg = r.body.error || `Error ${r.status}`;
      if(r.status === 401 || /credencial/i.test(errMsg) || /no encontrado/i.test(errMsg)){
        out.innerHTML = `${errMsg}. <button id="to-register" class="suggest-btn">Registrarse</button>`;
        out.classList.add('err');
        // agregar listener al botón para enfocar el formulario de registro
        setTimeout(()=>{
            const btn = document.getElementById('to-register');
            if(btn){
              btn.addEventListener('click', ()=>{
                const regInput = document.getElementById('register-username');
                if(regInput){
                  regInput.focus();
                  regInput.scrollIntoView({behavior:'smooth', block:'center'});
                }
              });
            }
          }, 0);
      }else{
        out.textContent = errMsg;
        out.classList.add('err');
      }
    }
  }catch(err){
    out.textContent = 'Error de conexión';
    out.classList.add('err');
  }
    btn.disabled = false;
    btn.innerHTML = 'Ingresar';
});

el('check-token').addEventListener('click', ()=>{
  const token = localStorage.getItem('access_token');
  alert(token ? `Token: ${token}` : 'No hay token guardado');
});

el('logout').addEventListener('click', ()=>{
  localStorage.removeItem('access_token');
  alert('Token eliminado');
});

// Botón del CTA estático que abre/enfoca el formulario de registro
const openRegisterBtn = document.getElementById('open-register');
if(openRegisterBtn){
  openRegisterBtn.addEventListener('click', (e)=>{
    e.preventDefault();
    const regSection = document.getElementById('register-section');
    const regInput = document.getElementById('register-username');
    if(regSection){
      // hacer scroll suavemente hacia la sección de registro
      regSection.scrollIntoView({behavior:'smooth', block:'center'});
    }
    if(regInput){
      setTimeout(()=> regInput.focus(), 300);
    }
  });
}

// Handler del botón de logout dentro del panel de cuenta
const logoutBtn = document.getElementById('logout-button');
if(logoutBtn){
  logoutBtn.addEventListener('click', ()=>{
    localStorage.removeItem('access_token');
    const acctCard = document.getElementById('account-card');
    if(acctCard) acctCard.classList.add('hidden');
    showToast('Sesión cerrada');
  });
}

// Refresh account (traer lista /users y actualizar datos)
const refreshBtn = document.getElementById('refresh-account');
if(refreshBtn){
  refreshBtn.addEventListener('click', async ()=>{
    const token = localStorage.getItem('access_token');
    const out = document.getElementById('account-result');
    out.textContent = '';
    if(!token){ out.textContent = 'No estás autenticado'; return; }
    refreshBtn.disabled = true; refreshBtn.innerHTML = '<span class="loader"></span> Cargando';
    try{
      const resp = await fetch(API_BASE + '/users', { headers: { 'Authorization': 'Bearer ' + token } });
      if(resp.ok){
        const users = await resp.json();
        const info = decodeJwt(token) || {};
        const acctId = info.sub || info.user_id || info.identity || info.id || '';
        const me = users.find(u => String(u.id) === String(acctId));
        if(me){
          document.getElementById('acct-id').textContent = me.id;
          document.getElementById('acct-username').textContent = me.username;
          out.textContent = 'Datos actualizados'; out.className='result ok';
        }else{ out.textContent = 'Usuario no encontrado'; out.className='result err'; }
      }else{ out.textContent = 'Error al consultar usuarios'; out.className='result err'; }
    }catch(e){ out.textContent = 'Error de conexión'; out.className='result err'; }
    refreshBtn.disabled = false; refreshBtn.innerHTML = 'Actualizar';
  });
}
