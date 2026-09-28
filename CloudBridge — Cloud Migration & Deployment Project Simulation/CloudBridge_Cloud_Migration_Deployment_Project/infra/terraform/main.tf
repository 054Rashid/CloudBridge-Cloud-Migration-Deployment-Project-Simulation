terraform {
  required_version = ">= 1.6.0"
  required_providers {
    aws = { source = "hashicorp/aws", version = "~> 5.0" }
  }
}

provider "aws" { region = var.aws_region }

variable "aws_region" {
  type = string
  default = "ap-south-1"
  description = "Target region used in this portfolio simulation."
}

variable "project_name" {
  type = string
  default = "cloudbridge"
}

module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "5.17.0"
  name = "${var.project_name}-vpc"
  cidr = "10.20.0.0/16"
  azs = ["${var.aws_region}a", "${var.aws_region}b"]
  private_subnets = ["10.20.1.0/24", "10.20.2.0/24"]
  public_subnets  = ["10.20.101.0/24", "10.20.102.0/24"]
  enable_nat_gateway = true
  single_nat_gateway = true
}

module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "20.37.1"
  cluster_name    = "${var.project_name}-eks"
  cluster_version = "1.31"
  vpc_id     = module.vpc.vpc_id
  subnet_ids = module.vpc.private_subnets
  eks_managed_node_groups = {
    default = {
      instance_types = ["t3.small"]
      min_size = 2
      max_size = 4
      desired_size = 2
    }
  }
}
