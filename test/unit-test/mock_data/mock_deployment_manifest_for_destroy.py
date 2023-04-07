deployment_manifest = {
    "name": "mlops",
    "toolchain_region": "us-east-1",
    "groups": [
        {
            "name": "optionals",
            "path": "manifests/mlops/optional-modules.yaml",
            "modules": [
                {
                    "name": "networking",
                    "path": "modules/optionals/networking/",
                    
                    
                    
                    "parameters": [
                        {
                            
                            "name": "internet-accessible",
                            "value": True
                        }
                    ],
                    
                    "target_account": "primary",
                    "target_region": "us-east-1",
                    
                },
                {
                    "name": "datalake-buckets",
                    "path": "modules/optionals/datalake-buckets",
                    
                    
                    
                    "parameters": [
                        {
                            
                            "name": "encryption-type",
                            "value": "SSE"
                        }
                    ],
                    
                    "target_account": "primary",
                    "target_region": "us-east-1",
                    
                }
            ],
            
        },
        {
            "name": "core",
            "path": "manifests/mlops/core-modules.yaml",
            "modules": [
                {
                    "name": "eks",
                    "path": "modules/core/eks/",
                    
                    
                    
                    "parameters": [
                        {
                            "value_from": {
                                "module_metadata": {
                                    "name": "networking",
                                    "group": "optionals",
                                    "key": "VpcId"
                                },
                                
                                
                               
                                
                            },
                            "name": "vpc-id",
                            
                        },
                        {
                            "value_from": {
                                "module_metadata": {
                                    "name": "networking",
                                    "group": "optionals",
                                    "key": "PrivateSubnetIds"
                                },
                                
                                
                               
                                
                            },
                            "name": "private-subnet-ids",
                            
                        },
                        {
                            
                            "name": "eks-admin-role-name",
                            "value": "Admin"
                        },
                        {
                            
                            "name": "eks-compute",
                            "value": {
                                "eks_nodegroup_config": [
                                    {
                                        "eks_ng_name": "ng1",
                                        "eks_node_quantity": 3,
                                        "eks_node_max_quantity": 6,
                                        "eks_node_min_quantity": 2,
                                        "eks_node_disk_size": 50,
                                        "eks_node_instance_types": [
                                            "m5.large"
                                        ]
                                    }
                                ],
                                "eks_version": 1.23,
                                "eks_node_spot": False
                            }
                        },
                        {
                            
                            "name": "eks-addons",
                            "value": {
                                "deploy_aws_lb_controller": True,
                                "deploy_external_dns": True,
                                "deploy_aws_ebs_csi": True,
                                "deploy_aws_efs_csi": True,
                                "deploy_aws_fsx_csi": True,
                                "deploy_cluster_autoscaler": True,
                                "deploy_metrics_server": True,
                                "deploy_secretsmanager_csi": True,
                                "deploy_external_secrets": False,
                                "deploy_cloudwatch_container_insights_metrics": True,
                                "deploy_cloudwatch_container_insights_logs": False,
                                "cloudwatch_container_insights_logs_retention_days": 7,
                                "deploy_amp": False,
                                "deploy_grafana_for_amp": False
                            }
                        }
                    ],
                    
                    "target_account": "primary",
                    "target_region": "us-east-1",
                    
                },
                {
                    "name": "efs",
                    "path": "modules/core/efs",
                    
                    
                    
                    "parameters": [
                        {
                            "value_from": {
                                "module_metadata": {
                                    "name": "networking",
                                    "group": "optionals",
                                    "key": "VpcId"
                                },
                                
                                
                               
                                
                            },
                            "name": "vpc-id",
                            
                        },
                        {
                            
                            "name": "removal-policy",
                            "value": "DESTROY"
                        }
                    ],
                    
                    "target_account": "primary",
                    "target_region": "us-east-1",
                    
                }
            ],
            
        },
        {
            "name": "platform",
            "path": "manifests/mlops/kf-platform.yaml",
            "modules": [
                {
                    "name": "kubeflow-platform",
                    "path": "modules/mlops/kubeflow-platform/",
                    
                    
                    
                    "parameters": [
                        {
                            "value_from": {
                                "module_metadata": {
                                    "name": "eks",
                                    "group": "core",
                                    "key": "EksClusterMasterRoleArn"
                                },
                                
                                
                               
                                
                            },
                            "name": "EksClusterMasterRoleArn",
                            
                        },
                        {
                            "value_from": {
                                "module_metadata": {
                                    "name": "eks",
                                    "group": "core",
                                    "key": "EksClusterName"
                                },
                                
                                
                               
                                
                            },
                            "name": "EksClusterName",
                            
                        },
                        {
                            
                            "name": "InstallationOption",
                            "value": "kustomize"
                        },
                        {
                            
                            "name": "DeploymentOption",
                            "value": "vanilla"
                        },
                        {
                            
                            "name": "KubeflowReleaseVersion",
                            "value": "v1.6.1"
                        },
                        {
                            
                            "name": "AwsKubeflowBuild",
                            "value": "1.0.0"
                        }
                    ],
                    
                    "target_account": "primary",
                    "target_region": "us-east-1",
                    
                },
                {
                    "name": "efs-on-eks",
                    "path": "modules/integration/efs-on-eks",
                    
                    
                    
                    "parameters": [
                        {
                            "value_from": {
                                "module_metadata": {
                                    "name": "eks",
                                    "group": "core",
                                    "key": "EksClusterAdminRoleArn"
                                },
                                
                                
                               
                                
                            },
                            "name": "eks-cluster-admin-role-arn",
                            
                        },
                        {
                            "value_from": {
                                "module_metadata": {
                                    "name": "eks",
                                    "group": "core",
                                    "key": "EksClusterName"
                                },
                                
                                
                               
                                
                            },
                            "name": "eks-cluster-name",
                            
                        },
                        {
                            "value_from": {
                                "module_metadata": {
                                    "name": "eks",
                                    "group": "core",
                                    "key": "EksOidcArn"
                                },
                                
                                
                               
                                
                            },
                            "name": "eks-oidc-arn",
                            
                        },
                        {
                            "value_from": {
                                "module_metadata": {
                                    "name": "eks",
                                    "group": "core",
                                    "key": "EksClusterSecurityGroupId"
                                },
                                
                                
                               
                                
                            },
                            "name": "eks-cluster-security-group-id",
                            
                        },
                        {
                            "value_from": {
                                "module_metadata": {
                                    "name": "efs",
                                    "group": "core",
                                    "key": "EFSFileSystemId"
                                },
                                
                                
                               
                                
                            },
                            "name": "efs-file-system-id",
                            
                        },
                        {
                            "value_from": {
                                "module_metadata": {
                                    "name": "efs",
                                    "group": "core",
                                    "key": "EFSSecurityGroupId"
                                },
                                
                                
                               
                                
                            },
                            "name": "efs-security-group-id",
                            
                        },
                        {
                            "value_from": {
                                "module_metadata": {
                                    "name": "efs",
                                    "group": "core",
                                    "key": "VpcId"
                                },
                                
                                
                               
                                
                            },
                            "name": "vpc-id",
                            
                        }
                    ],
                    
                    "target_account": "primary",
                    "target_region": "us-east-1",
                    
                }
            ],
            
        },
    ],
    
    "target_account_mappings": [
        {
            "alias": "primary",
            "account_id": "123456789012",
            "default": True,
            "parameters_global": {
                "dockerCredentialsSecret": "aws-addf-docker-credentials"
            },
            "region_mappings": [
                {
                    "region": "us-east-1",
                    "default": True,
                    "parameters_regional": {},
                    
                    
                }
            ],
            
        }
    ]
}


destroy_manifest = {
  "name": "mlops",
  "toolchain_region": "us-east-1",
  "target_account_mappings": [
    {
      "alias": "primary",
      "account_id": "123456789012",
      "default": True,
      "parameters_global": {
        "dockerCredentialsSecret": "aws-addf-docker-credentials"
      },
      "region_mappings": [
        {
          "region": "us-east-1",
          "default": True,
          "parameters_regional": {},
        }
      ]
    }
  ],
  "groups": [
    {
      "name": "users",
      "modules": [
        {
          "name": "kubeflow-users",
          "path": "modules/mlops/kubeflow-users",
          "bundle_md5": "03c4cce1b534053ab2e9907c00ffef3e",
          "manifest_md5": "d3e04a0cffa57cef83a57fb4f077ad50",
          "deployspec_md5": "b13401fb18d61964e1e39e2a1474a205",
          "parameters": [
            {
              "value_from": {
                "module_metadata": {
                  "name": "eks",
                  "group": "core",
                  "key": "EksClusterAdminRoleArn"
                },
              },
              "name": "EksClusterAdminRoleArn",
            },
            {
              "value_from": {
                "module_metadata": {
                  "name": "eks",
                  "group": "core",
                  "key": "EksClusterName"
                }
              },
              "name": "EksClusterName",
            },
            {
              "value_from": {
                "module_metadata": {
                  "name": "eks",
                  "group": "core",
                  "key": "EksOidcArn"
                }
              },
              "name": "EksOidcArn",
            },
            {
              "value_from": {
                "module_metadata": {
                  "name": "eks",
                  "group": "core",
                  "key": "EksClusterOpenIdConnectIssuer"
                }
              },
              "name": "EksClusterOpenIdConnectIssuer",
            },
            {
              "name": "KubeflowUsers",
              "value": [
                {
                  "policyArn": "arn:aws:iam::aws:policy/AdministratorAccess",
                  "secret": "addf-dataservice-users-kubeflow-users-kf-dgraeber"
                }
              ]
            }
          ],
          "deploy_spec": {
            "deploy": {
              "phases": {
                "install": {
                  "commands": [
                    "npm install -g aws-cdk@2.20.0",
                    "pip install -r requirements.txt",
                    "wget https://github.com/kubernetes-sigs/kustomize/releases/download/kustomize/v3.2.1/kustomize_kustomize.v3.2.1_linux_amd64",
                    "chmod +x kustomize_kustomize.v3.2.1_linux_amd64",
                    "mv kustomize_kustomize.v3.2.1_linux_amd64 /usr/local/bin/kustomize",
                    "kustomize version"
                  ]
                },
                "pre_build": { "commands": [] },
                "build": {
                  "commands": [
                    "echo 'Hi'"
                  ]
                },
                "post_build": { "commands": ["echo \"Deploy successful\""] }
              }
            },
            "destroy": {
              "phases": {
                "install": {
                  "commands": [
                    "npm install -g aws-cdk@2.20.0",
                    "pip install -r requirements.txt"
                  ]
                },
                "pre_build": { "commands": [] },
                "build": {
                  "commands": [
                    "if [[ ${ADDF_PARAMETER_KUBEFLOW_USERS} ]]; then\n  cdk destroy --force --app \"python app.py\";\nfi;\n"
                  ]
                },
                "post_build": { "commands": [] }
              }
            },
            "build_type": "BUILD_GENERAL1_SMALL",
            "publish_generic_env_variables": False
          },
          "target_account": "primary",
          "target_region": "us-east-1"
        }
      ]
    }
  ]
}


module_dependencies={'optionals-networking': ['core-eks', 'core-efs'], 'core-eks': ['platform-kubeflow-platform', 'platform-efs-on-eks'], 'core-efs': ['platform-efs-on-eks']}