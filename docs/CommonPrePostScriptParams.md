# CommonPrePostScriptParams

Specifies the path to the remote script and any common parameters expected by the remote script.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_active** | **bool** | Specifies whether the script should be enabled, default value set to true. | [optional] 
**params** | **str** | Specifies the arguments or parameters and values to pass into the remote script. For example if the script expects values for the &#39;database&#39; and &#39;user&#39; parameters, specify the parameters and values using the following string: \&quot;database&#x3D;myDatabase user&#x3D;me\&quot;. | [optional] 
**path** | **str** | Specifies the absolute path to the script on the remote host. | 
**timeout_secs** | **int** | Specifies the timeout of the script in seconds. The script will be killed if it exceeds this value. By default, no timeout will occur if left empty. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.common_pre_post_script_params import CommonPrePostScriptParams

# TODO update the JSON string below
json = "{}"
# create an instance of CommonPrePostScriptParams from a JSON string
common_pre_post_script_params_instance = CommonPrePostScriptParams.from_json(json)
# print the JSON string representation of the object
print(CommonPrePostScriptParams.to_json())

# convert the object into a dict
common_pre_post_script_params_dict = common_pre_post_script_params_instance.to_dict()
# create an instance of CommonPrePostScriptParams from a dict
common_pre_post_script_params_from_dict = CommonPrePostScriptParams.from_dict(common_pre_post_script_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


