// Verifica se o navegador suporta Service Workers
if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    navigator.serviceWorker.register('/static/service-worker.js')
      .then(registration => {
        console.log('Service Worker registrado com sucesso:', registration.scope);
      })
      .catch(error => {
        console.log('Falha ao registrar Service Worker:', error);
      });
  });
}

// Detecta se é um dispositivo móvel
function isMobileDevice() {
  return (typeof window.orientation !== "undefined") || (navigator.userAgent.indexOf('IEMobile') !== -1);
}

// Botão de instalação do PWA
let deferredPrompt;
const installButton = document.getElementById('install-button');

window.addEventListener('beforeinstallprompt', (e) => {
  // Previne que o prompt apareça automaticamente
  e.preventDefault();
  deferredPrompt = e;
  
  // Mostra botão de instalação se for mobile
  if (isMobileDevice() && installButton) {
    installButton.style.display = 'block';
    
    installButton.addEventListener('click', () => {
      // Esconde o botão
      installButton.style.display = 'none';
      
      // Mostra o prompt de instalação
      deferredPrompt.prompt();
      
      // Aguarda a resposta do usuário
      deferredPrompt.userChoice.then((choiceResult) => {
        if (choiceResult.outcome === 'accepted') {
          console.log('Usuário aceitou instalar o PWA');
        } else {
          console.log('Usuário recusou instalar o PWA');
        }
        deferredPrompt = null;
      });
    });
  }
});

// Detecta se o app está instalado
window.addEventListener('appinstalled', () => {
  console.log('PWA instalado com sucesso');
  if (installButton) {
    installButton.style.display = 'none';
  }
});

// Verifica modo de exibição
function displayMode() {
  if (window.matchMedia('(display-mode: standalone)').matches) {
    console.log('Executando como PWA instalado');
    return 'standalone';
  }
  return 'browser';
}

// Notificação de novo conteúdo (exemplo)
function showUpdateNotification() {
  if ('Notification' in window && Notification.permission === 'granted') {
    new Notification('Novo conteúdo disponível!', {
      body: 'Confira as últimas postagens no blog.',
      icon: '/static/icons/icon-192x192.png'
    });
  }
}

// Solicita permissão para notificações
function requestNotificationPermission() {
  if ('Notification' in window) {
    Notification.requestPermission().then(permission => {
      console.log('Permissão de notificação:', permission);
    });
  }
}

// Verifica conexão
function checkConnection() {
  if (!navigator.onLine) {
    console.log('Modo offline ativado');
    document.body.classList.add('offline');
  }
  
  window.addEventListener('online', () => {
    console.log('Voltou online');
    document.body.classList.remove('offline');
  });
  
  window.addEventListener('offline', () => {
    console.log('Ficou offline');
    document.body.classList.add('offline');
  });
}

// Inicializa funcionalidades PWA
document.addEventListener('DOMContentLoaded', () => {
  checkConnection();
  
  // Solicita permissão para notificações após algum tempo
  setTimeout(requestNotificationPermission, 5000);
});