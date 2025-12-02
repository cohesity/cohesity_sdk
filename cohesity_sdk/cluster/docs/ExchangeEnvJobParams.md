# ExchangeEnvJobParams

Specifies job parameters applicable for all 'kExchange' Environment type Protection Sources in a Protection Job.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backups_copy_only** | **bool** |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.exchange_env_job_params import ExchangeEnvJobParams

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangeEnvJobParams from a JSON string
exchange_env_job_params_instance = ExchangeEnvJobParams.from_json(json)
# print the JSON string representation of the object
print(ExchangeEnvJobParams.to_json())

# convert the object into a dict
exchange_env_job_params_dict = exchange_env_job_params_instance.to_dict()
# create an instance of ExchangeEnvJobParams from a dict
exchange_env_job_params_from_dict = ExchangeEnvJobParams.from_dict(exchange_env_job_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


