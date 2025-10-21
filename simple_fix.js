// Sencilla solución para habilitar la pestaña de Calculation Formulas en el Dashboard Enhanced

// Esperamos a que el documento esté completamente cargado
document.addEventListener('DOMContentLoaded', function() {
  // Esperar un poco para asegurarse de que todos los controladores se han inicializado
  setTimeout(function() {
    console.log('🛠️ Aplicando solución para la pestaña de Calculation Formulas');
    
    // 1. Añadimos el event listener para el tab de fórmulas
    const formulaTab = document.querySelector('[data-tab="formulas"]');
    if (formulaTab) {
      console.log('✅ Tab de fórmulas encontrado');
      
      // 2. Verificamos que el panel de fórmulas existe
      const formulaPanel = document.querySelector('#tab-formulas');
      if (formulaPanel) {
        console.log('✅ Panel de fórmulas encontrado');
        
        // 3. Asociamos las funciones de forma segura
        const saveBtn = document.getElementById('save-formula-config');
        const resetBtn = document.getElementById('reset-formula-config');
        const testBtn = document.getElementById('test-formula-config');
        const progressSelect = document.getElementById('formula-progress-method');
        const globalSelect = document.getElementById('formula-global-method');
        
        if (saveBtn) saveBtn.addEventListener('click', saveFormulaConfig);
        if (resetBtn) resetBtn.addEventListener('click', resetFormulaConfig);
        if (testBtn) testBtn.addEventListener('click', testFormulaConfig);
        if (progressSelect) progressSelect.addEventListener('change', updateFormulaLabels);
        if (globalSelect) globalSelect.addEventListener('change', updateFormulaLabels);
        
        // 4. Añadimos handler para cuando se cambia al tab de fórmulas
        formulaTab.addEventListener('click', function() {
          setTimeout(loadFormulaConfig, 100); // Pequeño retraso para asegurar que el panel esté visible
        });
        
        console.log('✅ Event listeners configurados correctamente');
      } else {
        console.error('❌ Panel de fórmulas no encontrado');
      }
    } else {
      console.error('❌ Tab de fórmulas no encontrado');
    }
  }, 500); // Espera medio segundo para asegurar que el DOM está completamente listo
});

// Función para guardar la configuración de fórmulas
function saveFormulaConfig() {
  console.log('Guardando configuración de fórmulas');
  
  try {
    // Recoger todos los valores del formulario
    const formulaConfig = {
      progressMethod: document.getElementById('formula-progress-method').value,
      globalMethod: document.getElementById('formula-global-method').value,
      statusInclusion: {
        TBS: document.getElementById('include-status-tbs').checked,
        WIP: document.getElementById('include-status-wip').checked,
        CLO: document.getElementById('include-status-clo').checked
      },
      weights: {
        min: parseFloat(document.getElementById('weight-min').value),
        max: parseFloat(document.getElementById('weight-max').value),
        default: parseFloat(document.getElementById('weight-default').value)
      },
      criticalityMultipliers: {
        low: parseFloat(document.getElementById('crit-low').value),
        medium: parseFloat(document.getElementById('crit-medium').value),
        high: parseFloat(document.getElementById('crit-high').value)
      },
      timestamp: new Date().toISOString()
    };
    
    // Guardar en localStorage
    localStorage.setItem('dashboard_formula_config', JSON.stringify(formulaConfig));
    
    // Mostrar confirmación
    alert('✅ Configuración de fórmulas guardada correctamente');
    
    // Si Dashboard.UIController existe, refrescar la UI
    if (window.Dashboard && window.Dashboard.UIController && window.Dashboard.UIController.apply) {
      window.Dashboard.UIController.apply();
    }
  } catch (err) {
    console.error('Error al guardar configuración:', err);
    alert('❌ Error al guardar la configuración');
  }
}

// Función para resetear a valores por defecto
function resetFormulaConfig() {
  console.log('Reseteando configuración de fórmulas');
  
  try {
    // Configuración por defecto
    const defaultConfig = {
      progressMethod: 'weighted',
      globalMethod: 'weighted',
      statusInclusion: {
        TBS: false,
        WIP: true,
        CLO: true
      },
      weights: {
        min: 0.5,
        max: 3.0,
        default: 1.0
      },
      criticalityMultipliers: {
        low: 1.0,
        medium: 1.0,
        high: 1.2
      },
      timestamp: new Date().toISOString()
    };
    
    // Aplicar valores al formulario
    document.getElementById('formula-progress-method').value = defaultConfig.progressMethod;
    document.getElementById('formula-global-method').value = defaultConfig.globalMethod;
    document.getElementById('include-status-tbs').checked = defaultConfig.statusInclusion.TBS;
    document.getElementById('include-status-wip').checked = defaultConfig.statusInclusion.WIP;
    document.getElementById('include-status-clo').checked = defaultConfig.statusInclusion.CLO;
    document.getElementById('weight-min').value = defaultConfig.weights.min;
    document.getElementById('weight-max').value = defaultConfig.weights.max;
    document.getElementById('weight-default').value = defaultConfig.weights.default;
    document.getElementById('crit-low').value = defaultConfig.criticalityMultipliers.low;
    document.getElementById('crit-medium').value = defaultConfig.criticalityMultipliers.medium;
    document.getElementById('crit-high').value = defaultConfig.criticalityMultipliers.high;
    
    // Guardar a localStorage
    localStorage.setItem('dashboard_formula_config', JSON.stringify(defaultConfig));
    
    // Actualizar etiquetas
    updateFormulaLabels();
    
    // Mostrar confirmación
    alert('⚠️ Configuración de fórmulas reseteada a valores por defecto');
  } catch (err) {
    console.error('Error al resetear configuración:', err);
    alert('❌ Error al resetear la configuración');
  }
}

// Función para probar la configuración actual
function testFormulaConfig() {
  console.log('Probando configuración de fórmulas');
  
  try {
    // Obtener configuración actual del formulario
    const formulaConfig = {
      progressMethod: document.getElementById('formula-progress-method').value,
      globalMethod: document.getElementById('formula-global-method').value,
      statusInclusion: {
        TBS: document.getElementById('include-status-tbs').checked,
        WIP: document.getElementById('include-status-wip').checked,
        CLO: document.getElementById('include-status-clo').checked
      }
    };
    
    // Obtener datos - usar Dashboard API si está disponible
    let buses = [], apps = [];
    if (window.Dashboard && window.Dashboard.StorageManager) {
      buses = window.Dashboard.StorageManager.getBUs();
      apps = window.Dashboard.StorageManager.getAllApps();
    }
    
    // Si no hay datos, mostrar mensaje
    if (buses.length === 0) {
      alert('⚠️ No hay datos para probar la configuración');
      return;
    }
    
    // Generar resultados de prueba
    let results = '<div style="padding: 16px; max-height: 500px; overflow-y: auto;">';
    results += '<h3>Resultados de prueba de fórmulas</h3>';
    results += '<p>Probando cálculo con configuración actual:</p>';
    results += '<ul>';
    results += `<li>Método de Progreso: <strong>${formulaConfig.progressMethod}</strong></li>`;
    results += `<li>Método Global: <strong>${formulaConfig.globalMethod}</strong></li>`;
    results += `<li>Incluir TBS: <strong>${formulaConfig.statusInclusion.TBS}</strong></li>`;
    results += `<li>Incluir WIP: <strong>${formulaConfig.statusInclusion.WIP}</strong></li>`;
    results += `<li>Incluir CLO: <strong>${formulaConfig.statusInclusion.CLO}</strong></li>`;
    results += '</ul>';
    
    // Calcular para cada BU
    results += '<table style="width:100%; border-collapse: collapse; margin-top: 16px;">';
    results += '<thead><tr style="background: var(--ring);"><th style="text-align:left; padding: 8px;">Unidad de Negocio</th><th style="text-align:center; padding: 8px;">Apps</th><th style="text-align:center; padding: 8px;">Progreso</th></tr></thead>';
    results += '<tbody>';
    
    let totalApps = 0;
    let weightedSum = 0;
    let buSum = 0;
    
    buses.forEach(bu => {
      const buApps = apps.filter(app => app.buId === bu.id);
      const buAppCount = buApps.length;
      totalApps += buAppCount;
      
      // Filtrar por estado según configuración
      const filteredApps = buApps.filter(app => {
        if (app.status === 'TBS' && !formulaConfig.statusInclusion.TBS) return false;
        if (app.status === 'WIP' && !formulaConfig.statusInclusion.WIP) return false;
        if (app.status === 'CLO' && !formulaConfig.statusInclusion.CLO) return false;
        return true;
      });
      
      // Calcular progreso BU según método seleccionado
      let buProgress = 0;
      
      if (filteredApps.length > 0) {
        if (formulaConfig.progressMethod === 'weighted') {
          const totalWeight = filteredApps.reduce((sum, app) => sum + (app.weight || 1), 0);
          const weightedSum = filteredApps.reduce((sum, app) => sum + ((app.progress || 0) * (app.weight || 1)), 0);
          buProgress = totalWeight > 0 ? Math.round(weightedSum / totalWeight) : 0;
        } else if (formulaConfig.progressMethod === 'simple') {
          buProgress = Math.round(filteredApps.reduce((sum, app) => sum + (app.progress || 0), 0) / filteredApps.length);
        } else if (formulaConfig.progressMethod === 'minimum') {
          buProgress = Math.min(...filteredApps.map(app => app.progress || 0));
        }
      }
      
      weightedSum += buProgress * buAppCount;
      buSum += buProgress;
      
      // Color de fondo basado en progreso
      const bgColor = buProgress === 100 ? 'rgba(50, 230, 133, 0.15)' : 
                     buProgress >= 50 ? 'rgba(255, 209, 102, 0.15)' : 
                     'rgba(255, 95, 122, 0.15)';
      
      results += `<tr style="background: ${bgColor}; border-bottom: 1px solid var(--ring);">
                   <td style="padding: 8px;">${bu.name}</td>
                   <td style="text-align:center; padding: 8px;">${buAppCount}</td>
                   <td style="text-align:center; padding: 8px;">${buProgress}%</td>
                 </tr>`;
    });
    
    results += '</tbody></table>';
    
    // Calcular progreso global
    const globalProgress = formulaConfig.globalMethod === 'weighted' 
      ? (totalApps > 0 ? Math.round(weightedSum / totalApps) : 0)
      : (buses.length > 0 ? Math.round(buSum / buses.length) : 0);
    
    results += `<div style="margin-top: 24px; background: var(--ring); padding: 16px; border-radius: 8px;">
                 <h4 style="margin-top:0;">Progreso Global: ${globalProgress}%</h4>
                 <p>Calculado usando: ${formulaConfig.globalMethod === 'weighted' ? 'Ponderado por Tamaño de BU' : 'Promedio Simple de BUs'}</p>
                 <div style="background: var(--panel); height: 24px; width: 100%; border-radius: 12px; overflow: hidden; margin-top: 8px;">
                   <div style="background: ${globalProgress === 100 ? 'var(--ok)' : globalProgress >= 50 ? 'var(--warn)' : 'var(--danger)'}; 
                               height: 100%; width: ${globalProgress}%"></div>
                 </div>
               </div>`;
    
    results += '</div>';
    
    // Mostrar resultados en modal
    showModalContent(results);
  } catch (err) {
    console.error('Error al probar configuración:', err);
    alert('❌ Error al probar la configuración');
  }
}

// Función para mostrar contenido en modal
function showModalContent(content) {
  // Verificar si ya existe un modal
  let nestedModal = document.querySelector('.nested-modal');
  
  // Si no existe, crearlo
  if (!nestedModal) {
    nestedModal = document.createElement('div');
    nestedModal.className = 'nested-modal';
    document.body.appendChild(nestedModal);
  }
  
  // Configurar y mostrar
  nestedModal.style.opacity = '1';
  nestedModal.style.pointerEvents = 'auto';
  
  nestedModal.innerHTML = `
    <div class="nested-modal-content" style="background: var(--panel); border: 1px solid var(--ring); 
        width: 80%; max-width: 800px; border-radius: var(--radius); box-shadow: 0 10px 50px rgba(0,0,0,0.5);">
      ${content}
      <div style="padding: 16px; display: flex; justify-content: flex-end;">
        <button class="btn btn-secondary" onclick="document.querySelector('.nested-modal').style.opacity='0'; document.querySelector('.nested-modal').style.pointerEvents='none';">
          Cerrar
        </button>
      </div>
    </div>
  `;
}

// Función para actualizar las etiquetas de fórmulas
function updateFormulaLabels() {
  console.log('Actualizando etiquetas de fórmulas');
  
  try {
    // Obtener método seleccionado
    const progressMethod = document.getElementById('formula-progress-method').value;
    const globalMethod = document.getElementById('formula-global-method').value;
    
    // Actualizar etiquetas de método de progreso
    document.querySelectorAll('.math-formula.weighted, .math-formula.simple, .math-formula.minimum').forEach(el => {
      el.style.display = 'none';
    });
    const progressFormulaEl = document.querySelector('.math-formula.' + progressMethod);
    if (progressFormulaEl) progressFormulaEl.style.display = 'block';
    
    // Actualizar etiquetas de método global
    document.querySelectorAll('.math-formula.global-weighted, .math-formula.global-simple').forEach(el => {
      el.style.display = 'none';
    });
    const globalFormulaEl = document.querySelector('.math-formula.global-' + globalMethod);
    if (globalFormulaEl) globalFormulaEl.style.display = 'block';
  } catch (err) {
    console.error('Error al actualizar etiquetas:', err);
  }
}

// Función para cargar la configuración guardada
function loadFormulaConfig() {
  console.log('Cargando configuración de fórmulas');
  
  try {
    // Intentar obtener configuración guardada
    const savedConfigStr = localStorage.getItem('dashboard_formula_config');
    
    // Si no hay configuración guardada, usar valores por defecto
    if (!savedConfigStr) {
      console.log('No se encontró configuración guardada, usando valores por defecto');
      resetFormulaConfig();
      return;
    }
    
    // Parsear configuración
    const config = JSON.parse(savedConfigStr);
    
    // Aplicar al formulario
    document.getElementById('formula-progress-method').value = config.progressMethod || 'weighted';
    document.getElementById('formula-global-method').value = config.globalMethod || 'weighted';
    
    // Inclusión de estados
    if (config.statusInclusion) {
      document.getElementById('include-status-tbs').checked = config.statusInclusion.TBS || false;
      document.getElementById('include-status-wip').checked = config.statusInclusion.WIP !== undefined ? config.statusInclusion.WIP : true;
      document.getElementById('include-status-clo').checked = config.statusInclusion.CLO !== undefined ? config.statusInclusion.CLO : true;
    }
    
    // Pesos
    if (config.weights) {
      document.getElementById('weight-min').value = config.weights.min || 0.5;
      document.getElementById('weight-max').value = config.weights.max || 3.0;
      document.getElementById('weight-default').value = config.weights.default || 1.0;
    }
    
    // Multiplicadores de criticidad
    if (config.criticalityMultipliers) {
      document.getElementById('crit-low').value = config.criticalityMultipliers.low || 1.0;
      document.getElementById('crit-medium').value = config.criticalityMultipliers.medium || 1.0;
      document.getElementById('crit-high').value = config.criticalityMultipliers.high || 1.2;
    }
    
    // Actualizar etiquetas de fórmulas
    updateFormulaLabels();
    
    console.log('✅ Configuración de fórmulas cargada correctamente');
  } catch (err) {
    console.error('Error al cargar configuración:', err);
    // Usar valores por defecto en caso de error
    resetFormulaConfig();
  }
}

// Añadir de forma segura el soporte para switchTab si el tab formulas es clickeado
document.addEventListener('click', function(event) {
  if (event.target && event.target.matches('[data-tab="formulas"]')) {
    // Si Dashboard.AdminController no está disponible, manejamos nosotros el tab
    if (!window.Dashboard || !window.Dashboard.AdminController || typeof window.Dashboard.AdminController.loadFormulaConfig !== 'function') {
      console.log('Cambiando a tab de fórmulas (manejador externo)');
      
      // Activar el tab
      Array.from(document.querySelectorAll('.modal-tab')).forEach(t => t.classList.remove('active'));
      Array.from(document.querySelectorAll('.modal-tabpanel')).forEach(p => p.classList.remove('active'));
      event.target.classList.add('active');
      
      const formulaPanel = document.querySelector('#tab-formulas');
      if (formulaPanel) {
        formulaPanel.classList.add('active');
        loadFormulaConfig();
      }
      
      // Prevenir comportamiento predeterminado si hemos manejado el evento
      event.stopPropagation();
    }
  }
});

console.log('🔧 Script de corrección para Calculation Formulas cargado');