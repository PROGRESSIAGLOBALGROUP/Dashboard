// Helper function to format priority as a semantic badge
formatPriorityBadge(priority) {
  const priority_str = String(priority || 'Medium');
  const badgeClass = priority_str === 'High' ? 'danger' : 
                     priority_str === 'Low' ? 'ok' : 'warn';
  const badgeEmoji = priority_str === 'High' ? '🔴' : 
                     priority_str === 'Low' ? '🟢' : '🟡';
  return `<span class="priority-badge priority-${priority_str.toLowerCase()}">${badgeEmoji} ${priority_str}</span>`;
},
