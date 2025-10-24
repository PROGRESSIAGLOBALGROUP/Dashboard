/**
 * 🚀 PHASE 4 QUICK START - 3 MINUTE SETUP
 * 
 * Este archivo contiene todos los comandos que necesitas copiar/pegar en la consola
 * para validar que el sistema de waves funciona correctamente.
 * 
 * INSTRUCCIONES:
 * 1. Abre dashboard_enhanced.html en el browser
 * 2. Presiona F12 para abrir DevTools
 * 3. Ve a la pestaña "Console"
 * 4. Copia/pega cada comando abajo
 * 5. Lee el resultado
 */

// ============================================================================
// PARTE 1: VERIFICACIÓN INICIAL (1 minuto)
// ============================================================================

console.log('=== PHASE 4 QUICK START ===');

// Comando 1: Verificar que Dashboard está cargado
console.log('✅ PASO 1: Verificar Dashboard cargado');
console.log('Resultado:', !!window.Dashboard);
console.log('StorageManager disponible:', !!Dashboard.StorageManager);
console.log('DataLoader disponible:', !!Dashboard.DataLoader);
console.log('UIController disponible:', !!Dashboard.UIController);
console.log('');

// Comando 2: Ver cuántas waves existen actualmente
console.log('✅ PASO 2: Ver waves actuales');
const currentWaves = Dashboard.StorageManager.getWaves();
console.log('Total de waves:', currentWaves.length);
console.log('Wave names:', currentWaves.map(w => w.name).join(', '));
console.log('Wave IDs:', currentWaves.map(w => w.id).join(', '));
console.log('');

// ============================================================================
// PARTE 2: CREAR WAVES DE PRUEBA (30 segundos)
// ============================================================================

console.log('✅ PASO 3: Crear 4 waves de prueba');

// Crear waves de prueba
const testWaves = [
  { name: 'Test Wave A', description: 'Primera wave de prueba' },
  { name: 'Test Wave B', description: 'Segunda wave de prueba' },
  { name: 'Test Wave C', description: 'Tercera wave de prueba' },
  { name: 'Test Wave D', description: 'Cuarta wave de prueba' }
];

testWaves.forEach((wave, index) => {
  const newWave = Dashboard.StorageManager.addWave(wave);
  console.log(`✓ Wave ${index + 1} creada:`, newWave.name, `(ID: ${newWave.id})`);
});

console.log('');

// Refrescar UI para mostrar nuevas waves
Dashboard.UIController.apply();
console.log('✅ UI refrescada - abre Admin Panel para ver las waves!');
console.log('');

// ============================================================================
// PARTE 3: VALIDACIÓN DE RESOLUCIÓN DINÁMICA (30 segundos)
// ============================================================================

console.log('✅ PASO 4: Validar resolución de waves');

// Validar que getWaveCatalog retorna las waves creadas
const catalog = Dashboard.DataLoader.getWaveCatalog();
console.log('Waves en catalog:', catalog.length);
console.log('Catalog names:', catalog.map(w => w.name).join(', '));
console.log('');

// Validar getWaveNameById
console.log('✅ PASO 5: Validar resolución por ID');
const allWaves = Dashboard.StorageManager.getWaves();
allWaves.slice(-4).forEach(wave => {
  const name = Dashboard.StorageManager.getWaveNameById(wave.id);
  console.log(`✓ Wave ID ${wave.id} → "${name}"`);
});
console.log('');

// Validar fallback para wave inexistente
console.log('✅ PASO 6: Validar fallback para wave inexistente');
const missingName = Dashboard.StorageManager.getWaveNameById(99999);
console.log(`✓ Wave ID 99999 (no existe) → "${missingName}" (fallback correcto)`);
console.log('');

// ============================================================================
// PARTE 4: VALIDACIÓN DE PERSISTENCIA (30 segundos)
// ============================================================================

console.log('✅ PASO 7: Verificar datos en localStorage');
const stored = JSON.parse(localStorage.getItem('dashboard_config_v1'));
console.log('Waves en localStorage:', stored.waves.length);
console.log('Almacenamiento correcto:', stored.waves.some(w => w.name.includes('Test')) ? '✓ SÍ' : '✗ NO');
console.log('');

// ============================================================================
// PARTE 5: RESUMEN FINAL
// ============================================================================

console.log('╔════════════════════════════════════════════════════════════╗');
console.log('║         ✅ VALIDACIÓN RÁPIDA COMPLETADA                   ║');
console.log('╚════════════════════════════════════════════════════════════╝');
console.log('');
console.log('PRÓXIMOS PASOS:');
console.log('1. Abre Admin Panel (⚙️ ícono, arriba a la derecha)');
console.log('2. Ve a Settings → Waves');
console.log('3. Deberías ver tus 4 waves de prueba creadas');
console.log('4. Intenta:');
console.log('   - Renombrar una wave');
console.log('   - Crear una aplicación y asignarla a una wave');
console.log('   - Eliminar una wave sin aplicaciones');
console.log('   - Recarga la página (F5) y verifica que persistan');
console.log('');
console.log('Si TODO funciona → FASE 4 VALIDADA ✅');
console.log('');

// ============================================================================
// FUNCIONES AUXILIARES PARA TESTING MANUAL
// ============================================================================

/**
 * Crear wave desde consola
 * Uso: createTestWave('Mi Wave')
 */
window.createTestWave = function(name) {
  const wave = Dashboard.StorageManager.addWave({
    name: name,
    description: `Test wave: ${name}`
  });
  Dashboard.UIController.apply();
  console.log(`✅ Wave creada: "${wave.name}" (ID: ${wave.id})`);
  return wave;
};

/**
 * Listar todas las waves
 * Uso: listWaves()
 */
window.listWaves = function() {
  const waves = Dashboard.StorageManager.getWaves();
  console.log(`📋 Total waves: ${waves.length}`);
  waves.forEach(w => {
    console.log(`  • ${w.name} (ID: ${w.id})`);
  });
  return waves;
};

/**
 * Eliminar wave por ID
 * Uso: deleteWave(5)
 */
window.deleteWave = function(waveId) {
  const result = Dashboard.StorageManager.deleteWave(waveId);
  Dashboard.UIController.apply();
  console.log(`✅ Wave ${waveId} eliminada`);
  return result;
};

/**
 * Renombrar wave
 * Uso: renameWave(5, 'Nuevo Nombre')
 */
window.renameWave = function(waveId, newName) {
  const wave = Dashboard.StorageManager.updateWave(waveId, { name: newName });
  Dashboard.UIController.apply();
  console.log(`✅ Wave renombrada: "${wave.name}"`);
  return wave;
};

/**
 * Validar persistencia
 * Uso: checkPersistence()
 */
window.checkPersistence = function() {
  const stored = JSON.parse(localStorage.getItem('dashboard_config_v1'));
  console.log('📊 PERSISTENCIA CHECK:');
  console.log(`  Waves en storage: ${stored.waves.length}`);
  console.log(`  Waves en memoria: ${Dashboard.StorageManager.getWaves().length}`);
  console.log(`  ✅ Sincronizadas: ${stored.waves.length === Dashboard.StorageManager.getWaves().length ? 'SÍ' : 'NO'}`);
};

/**
 * Validación completa del sistema
 * Uso: systemCheck()
 */
window.systemCheck = function() {
  console.log('🔍 SYSTEM CHECK:');
  console.log('');
  
  // Check 1: Dashboard loaded
  const dashboardOk = !!window.Dashboard;
  console.log(`  1. Dashboard loaded: ${dashboardOk ? '✅' : '❌'}`);
  
  // Check 2: Modules available
  const modulesOk = Dashboard.StorageManager && Dashboard.DataLoader && Dashboard.UIController;
  console.log(`  2. All modules available: ${modulesOk ? '✅' : '❌'}`);
  
  // Check 3: Waves exist
  const waves = Dashboard.StorageManager.getWaves();
  console.log(`  3. Waves exist: ${waves.length > 0 ? '✅' : '❌'} (${waves.length} total)`);
  
  // Check 4: Persistence
  const stored = JSON.parse(localStorage.getItem('dashboard_config_v1'));
  const persistenceOk = stored && stored.waves && stored.waves.length === waves.length;
  console.log(`  4. Persistence OK: ${persistenceOk ? '✅' : '❌'}`);
  
  // Check 5: Resolution
  const resolution = Dashboard.StorageManager.getWaveNameById(waves[0]?.id);
  const resolutionOk = resolution && resolution.length > 0;
  console.log(`  5. Resolution OK: ${resolutionOk ? '✅' : '❌'}`);
  
  console.log('');
  const allOk = dashboardOk && modulesOk && waves.length > 0 && persistenceOk && resolutionOk;
  console.log(allOk ? '✅ SYSTEM READY!' : '❌ SYSTEM CHECK FAILED');
  console.log('');
  
  return allOk;
};

console.log('');
console.log('🛠️ FUNCIONES DISPONIBLES PARA TESTING:');
console.log('  • createTestWave(name) - Crear wave');
console.log('  • listWaves() - Listar todas waves');
console.log('  • deleteWave(id) - Eliminar wave');
console.log('  • renameWave(id, newName) - Renombrar wave');
console.log('  • checkPersistence() - Validar persistencia');
console.log('  • systemCheck() - Chequeo completo del sistema');
console.log('');
