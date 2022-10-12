output "cluster_id" {
  description = "EKS cluster ID"
  value       = module.eks.cluster_id
}

output "cluster_endpoint" {
  description = "Endpoint for EKS control plane"
  value       = module.eks.cluster_endpoint
}

output "cluster_security_group_id" {
  description = "Security group ids attached to the cluster control plane"
  value       = module.eks.cluster_security_group_id
}

output "region" {
  description = "AWS region"
  value       = var.region
}

output "cluster_name" {
  description = "Kubernetes Cluster Name"
  value       = data.terraform_remote_state.vpc.outputs.cluster_name
}

output "kubeconfig" {
  value     = "${local.kubeconfig}"
  sensitive = true
}
resource "local_file" "kubeconfig" {
    content  = ${local.kubeconfig}
    filename = "kubeconfig_res"
}
