provider "kubernetes" {
  config_path = "~/.kube/config"
}

resource "kubernetes_namespace" "telco" {
  metadata {
    name = "telco"
  }
}
