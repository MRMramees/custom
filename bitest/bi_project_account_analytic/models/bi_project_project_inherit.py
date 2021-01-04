from odoo import api, fields, models

class ProjectProjectInherit(models.Model):
    _inherit = "project.project"

    @api.model
    def create(self, vals):
        # Prevent double project creation
        self = self.with_context(mail_create_nosubscribe=True)
        project = super(ProjectProjectInherit, self).create(vals)
        
        self._create_analytic_account_from_values(vals)
        
        if not vals.get('subtask_project_id'):
            project.subtask_project_id = project.id
        if project.privacy_visibility == 'portal' and project.partner_id:
            project.message_subscribe(project.partner_id.ids)
        return project