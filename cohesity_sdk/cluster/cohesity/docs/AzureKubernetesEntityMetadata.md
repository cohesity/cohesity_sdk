# AzureKubernetesEntityMetadata

Specifies the parameters to register a Kubernetes source.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_private_key** | **str** | Specifies the bearer token or private key of Kubernetes source. | 
**data_mover_image_location** | **str** | Specifies the datamover image location of Kubernetes source. | 
**datamover_service_type** | **str, none_type** | Specifies the data mover service type of Kubernetes source. | [optional] 
**init_container_image_location** | **str, none_type** | Specifies the initial container image location of Kubernetes source. | [optional] 
**san_fields** | **[str], none_type** | Specifies the SAN field for agent certificate. | [optional] 
**service_annotations** | [**[KubernetesServiceAnnotationObject], none_type**](KubernetesServiceAnnotationObject.md) | Specifies the service annotation object of Kubernetes source. | [optional] 
**velero_aws_plugin_image_location** | **str, none_type** | Specifies the velero AWS plugin image location of the Kubernetes source. | [optional] 
**velero_image_location** | **str, none_type** | Specifies the velero image location of the Kubernetes source. | [optional] 
**velero_kubevirt_plugin_image_location** | **str, none_type** | Specifies the velero kubevirt plugin image location of the Kubernetes source. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


