# KubernetesSourceRegistrationParams

Specifies the parameters to register a Kubernetes source.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_private_key** | **str** | Specifies the bearer token or private key of Kubernetes source. | 
**data_mover_image_location** | **str** | Specifies the datamover image location of Kubernetes source. | 
**endpoint** | **str** | Specifies the endpoint of Kubernetes source. | 
**kubernetes_distribution** | **str** | Specifies the distribution type of Kubernetes source. | 
**auto_protect_config** | [**KubernetesAutoProtectConfig**](KubernetesAutoProtectConfig.md) |  | [optional] 
**cohesity_dataprotect_plugin_image_location** | **str, none_type** | Specifies the custom Cohesity Dataprotect plugin image location of the Kubernetes source. | [optional] 
**datamover_service_type** | **str, none_type** | Specifies the data mover service type of Kubernetes source. | [optional] 
**default_vlan_params** | [**VlanParams**](VlanParams.md) |  | [optional] 
**init_container_image_location** | **str, none_type** | Specifies the initial container image location of Kubernetes source. | [optional] 
**kubernetes_type** | **str, none_type** | Specifies the type of kubernetes source | [optional] 
**priority_class_name** | **str, none_type** | Specifies the priority class name for cohesity resources. | [optional] 
**resource_annotations** | [**[KubernetesLabelObject], none_type**](KubernetesLabelObject.md) | Specifies resource annotations to be applied on cohesity resources. | [optional] 
**resource_labels** | [**[KubernetesLabelObject], none_type**](KubernetesLabelObject.md) | Specifies resource label to be applied on cohesity resources. | [optional] 
**san_fields** | **[str], none_type** | Specifies the SAN field for agent certificate. | [optional] 
**service_annotations** | [**[KubernetesServiceAnnotationObject], none_type**](KubernetesServiceAnnotationObject.md) | Specifies the service annotation object of Kubernetes source. | [optional] 
**velero_aws_plugin_image_location** | **str, none_type** | Specifies the velero AWS plugin image location of the Kubernetes source. | [optional] 
**velero_image_location** | **str, none_type** | Specifies the velero image location of the Kubernetes source. | [optional] 
**velero_kubevirt_plugin_image_location** | **str, none_type** | Specifies the velero kubevirt plugin image location of the Kubernetes source. | [optional] 
**velero_openshift_plugin_image_location** | **str, none_type** | Specifies the velero open shift plugin image for the Kubernetes source. | [optional] 
**vlan_info_vec** | [**[KubernetesVlanInfo], none_type**](KubernetesVlanInfo.md) | Specifies VLAN information provided during registration. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


