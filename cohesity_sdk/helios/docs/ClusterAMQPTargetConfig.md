# ClusterAMQPTargetConfig

Specifies the AMQP target config.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate** | **str** | Specifies the certificate. | [optional] 
**exchange** | **str** | Specifies the exchange. | [optional] 
**filer_id** | **int** | Specifies the filer id. | [optional] 
**password** | **str** | Specifies the password. | [optional] 
**server_ip** | **str** | Specifies the server ip. | [optional] 
**username** | **str** | Specifies the username. | [optional] 
**virtual_host** | **str** | Specifies the virtual host. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.cluster_amqp_target_config import ClusterAMQPTargetConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterAMQPTargetConfig from a JSON string
cluster_amqp_target_config_instance = ClusterAMQPTargetConfig.from_json(json)
# print the JSON string representation of the object
print(ClusterAMQPTargetConfig.to_json())

# convert the object into a dict
cluster_amqp_target_config_dict = cluster_amqp_target_config_instance.to_dict()
# create an instance of ClusterAMQPTargetConfig from a dict
cluster_amqp_target_config_from_dict = ClusterAMQPTargetConfig.from_dict(cluster_amqp_target_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


