# KubernetesSourceRegistrationParams

Specifies the parameters to register a Kubernetes source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_protect_config** | [**KubernetesAutoProtectConfig**](KubernetesAutoProtectConfig.md) |  | [optional] 
**client_private_key** | **str** | Specifies the bearer token or private key of Kubernetes source. | 
**cohesity_dataprotect_plugin_image_location** | **str** | Specifies the custom Cohesity Dataprotect plugin image location of the Kubernetes source. | [optional] 
**data_mover_image_location** | **str** | Specifies the datamover image location of Kubernetes source. | 
**datamover_service_type** | **str** | Specifies the data mover service type of Kubernetes source. | [optional] 
**default_vlan_params** | [**VlanParams**](VlanParams.md) |  | [optional] 
**endpoint** | **str** | Specifies the endpoint of Kubernetes source. | 
**init_container_image_location** | **str** | Specifies the initial container image location of Kubernetes source. | [optional] 
**kubernetes_distribution** | **str** | Specifies the distribution type of Kubernetes source. | 
**kubernetes_type** | **str** | Specifies the type of kubernetes source | [optional] 
**priority_class_name** | **str** | Specifies the priority class name for cohesity resources. | [optional] 
**resource_annotations** | [**List[KubernetesLabelObject]**](KubernetesLabelObject.md) | Specifies resource annotations to be applied on cohesity resources. | [optional] 
**resource_labels** | [**List[KubernetesLabelObject]**](KubernetesLabelObject.md) | Specifies resource label to be applied on cohesity resources. | [optional] 
**san_fields** | **List[str]** | Specifies the SAN field for agent certificate. | [optional] 
**service_annotations** | [**List[KubernetesServiceAnnotationObject]**](KubernetesServiceAnnotationObject.md) | Specifies the service annotation object of Kubernetes source. | [optional] 
**velero_aws_plugin_image_location** | **str** | Specifies the velero AWS plugin image location of the Kubernetes source. | [optional] 
**velero_image_location** | **str** | Specifies the velero image location of the Kubernetes source. | [optional] 
**velero_kubevirt_plugin_image_location** | **str** | Specifies the velero kubevirt plugin image location of the Kubernetes source. | [optional] 
**velero_openshift_plugin_image_location** | **str** | Specifies the velero open shift plugin image for the Kubernetes source. | [optional] 
**vlan_info_vec** | [**List[KubernetesVlanInfo]**](KubernetesVlanInfo.md) | Specifies VLAN information provided during registration. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.kubernetes_source_registration_params import KubernetesSourceRegistrationParams

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesSourceRegistrationParams from a JSON string
kubernetes_source_registration_params_instance = KubernetesSourceRegistrationParams.from_json(json)
# print the JSON string representation of the object
print(KubernetesSourceRegistrationParams.to_json())

# convert the object into a dict
kubernetes_source_registration_params_dict = kubernetes_source_registration_params_instance.to_dict()
# create an instance of KubernetesSourceRegistrationParams from a dict
kubernetes_source_registration_params_from_dict = KubernetesSourceRegistrationParams.from_dict(kubernetes_source_registration_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


