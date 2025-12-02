# AzureKubernetesEntityMetadata

Specifies the parameters to register a Kubernetes source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_private_key** | **str** | Specifies the bearer token or private key of Kubernetes source. | 
**data_mover_image_location** | **str** | Specifies the datamover image location of Kubernetes source. | 
**datamover_service_type** | **str** | Specifies the data mover service type of Kubernetes source. | [optional] 
**init_container_image_location** | **str** | Specifies the initial container image location of Kubernetes source. | [optional] 
**san_fields** | **List[str]** | Specifies the SAN field for agent certificate. | [optional] 
**service_annotations** | [**List[KubernetesServiceAnnotationObject]**](KubernetesServiceAnnotationObject.md) | Specifies the service annotation object of Kubernetes source. | [optional] 
**velero_aws_plugin_image_location** | **str** | Specifies the velero AWS plugin image location of the Kubernetes source. | [optional] 
**velero_image_location** | **str** | Specifies the velero image location of the Kubernetes source. | [optional] 
**velero_kubevirt_plugin_image_location** | **str** | Specifies the velero kubevirt plugin image location of the Kubernetes source. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.azure_kubernetes_entity_metadata import AzureKubernetesEntityMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of AzureKubernetesEntityMetadata from a JSON string
azure_kubernetes_entity_metadata_instance = AzureKubernetesEntityMetadata.from_json(json)
# print the JSON string representation of the object
print(AzureKubernetesEntityMetadata.to_json())

# convert the object into a dict
azure_kubernetes_entity_metadata_dict = azure_kubernetes_entity_metadata_instance.to_dict()
# create an instance of AzureKubernetesEntityMetadata from a dict
azure_kubernetes_entity_metadata_from_dict = AzureKubernetesEntityMetadata.from_dict(azure_kubernetes_entity_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


