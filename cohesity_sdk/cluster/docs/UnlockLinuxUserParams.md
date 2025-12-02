# UnlockLinuxUserParams

Specifies the Linux username whose account needs to be unlocked.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | Specifies the status of the linux user | [optional] 
**username** | **str** | The linux username to unlock. | 

## Example

```python
from cohesity_sdk.cluster.models.unlock_linux_user_params import UnlockLinuxUserParams

# TODO update the JSON string below
json = "{}"
# create an instance of UnlockLinuxUserParams from a JSON string
unlock_linux_user_params_instance = UnlockLinuxUserParams.from_json(json)
# print the JSON string representation of the object
print(UnlockLinuxUserParams.to_json())

# convert the object into a dict
unlock_linux_user_params_dict = unlock_linux_user_params_instance.to_dict()
# create an instance of UnlockLinuxUserParams from a dict
unlock_linux_user_params_from_dict = UnlockLinuxUserParams.from_dict(unlock_linux_user_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


