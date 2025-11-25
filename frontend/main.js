import './style.css'

const form = document.getElementById('freight-form');
const cepInput = document.getElementById('cep');
const resultsContainer = document.getElementById('results-container');
const resultsList = document.getElementById('results-list');
const loading = document.getElementById('loading');
const errorMessage = document.getElementById('error-message');

// Format CEP input
cepInput.addEventListener('input', (e) => {
  let value = e.target.value.replace(/\D/g, '');
  if (value.length > 5) {
    value = value.substring(0, 5) + '-' + value.substring(5, 8);
  }
  e.target.value = value;
});

form.addEventListener('submit', async (e) => {
  e.preventDefault();
  
  const cep = cepInput.value.replace(/\D/g, '');
  
  if (cep.length !== 8) {
    showError('Please enter a valid 8-digit CEP.');
    return;
  }

  showLoading();

  try {
    const response = await fetch(`/api/fretes?cep=${cep}`);
    
    if (!response.ok) {
      throw new Error('Failed to fetch shipping options');
    }

    const data = await response.json();
    
    if (data.error) {
      throw new Error(data.error);
    }

    renderResults(data.options);
  } catch (error) {
    showError(error.message || 'An error occurred while fetching shipping options.');
  } finally {
    hideLoading();
  }
});

function showLoading() {
  loading.classList.remove('hidden');
  resultsContainer.classList.add('hidden');
  errorMessage.classList.add('hidden');
}

function hideLoading() {
  loading.classList.add('hidden');
}

function showError(message) {
  errorMessage.textContent = message;
  errorMessage.classList.remove('hidden');
  resultsContainer.classList.add('hidden');
}

function renderResults(options) {
  resultsList.innerHTML = '';
  
  if (!options || options.length === 0) {
    showError('No shipping options found for this CEP.');
    return;
  }

  options.forEach(option => {
    const card = document.createElement('div');
    card.className = 'result-card';
    
    // Format currency
    const price = new Intl.NumberFormat('pt-BR', {
      style: 'currency',
      currency: 'BRL'
    }).format(option.price);

    // Format days
    const days = option.eta_days === 1 ? '1 day' : `${option.eta_days} days`;

    card.innerHTML = `
      <div class="provider-info">
        <h3>${option.provider}</h3>
        <p>${option.service}</p>
      </div>
      <div class="price-info">
        <div class="price">${price}</div>
        <div class="delivery-time">${days}</div>
      </div>
    `;
    
    resultsList.appendChild(card);
  });

  resultsContainer.classList.remove('hidden');
}
