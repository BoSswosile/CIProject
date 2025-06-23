provider "azurerm" {
  features {}
}

terraform {
  backend "azurerm" {
    resource_group_name  = cicd-final
    storage_account_name = cicdstoragegroupe2
    container_name       = "tfstate"
    key                  = "terraform.tfstate"
  }
}
