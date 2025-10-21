      html += `
        <tr>
          <td><input type="text" value="${app.name}" onchange="Dashboard.AdminController.updateApp(${app.id}, {name: this.value})"/></td>
          <td><select onchange="Dashboard.AdminController.updateApp(${app.id}, {status: this.value})">
            <option value="TBS" ${app.status === 'TBS' ? 'selected' : ''}>TBS</option>
            <option value="WIP" ${app.status === 'WIP' ? 'selected' : ''}>WIP</option>
            <option value="CLO" ${app.status === 'CLO' ? 'selected' : ''}>CLO</option>
          </select></td>
          <td><input type="number" min="0" max="100" value="${app.progress || 0}" onchange="Dashboard.AdminController.updateApp(${app.id}, {progress: parseInt(this.value)})"/></td>
          <td><span class="auto-weight">${Dashboard.ProgressCalculator.calculateAppWeight(app).toFixed(2)}</span></td>
          <td><select onchange="Dashboard.AdminController.updateApp(${app.id}, {criticality: this.value})">
            <option value="Low" ${app.criticality === 'Low' ? 'selected' : ''}>Low</option>
            <option value="Medium" ${app.criticality === 'Medium' ? 'selected' : ''}>Medium</option>
            <option value="High" ${app.criticality === 'High' ? 'selected' : ''}>High</option>
          </select></td>
          <td><select onchange="Dashboard.AdminController.updateApp(${app.id}, {businessImpact: this.value})">
            <option value="Low" ${app.businessImpact === 'Low' ? 'selected' : ''}>Low</option>
            <option value="Medium" ${(app.businessImpact === 'Medium' || !app.businessImpact) ? 'selected' : ''}>Medium</option>
            <option value="High" ${app.businessImpact === 'High' ? 'selected' : ''}>High</option>
          </select></td>
          <td><select onchange="Dashboard.AdminController.updateApp(${app.id}, {priority: this.value})">
            <option value="Low" ${app.priority === 'Low' ? 'selected' : ''}>Low</option>
            <option value="Medium" ${(app.priority === 'Medium' || !app.priority) ? 'selected' : ''}>Medium</option>
            <option value="High" ${app.priority === 'High' ? 'selected' : ''}>High</option>
          </select></td>
          <td><button class="btn btn-danger btn-sm" onclick="Dashboard.AdminController.deleteApp(${app.id})">Delete</button></td>
        </tr>`;