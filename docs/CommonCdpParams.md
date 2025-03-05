# CommonCdpParams

Specifies the params for Continuous Data Protection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_cdp_sync_replication** | **bool** | Specifies whether synchronous replication is enabled for CDP Protection Group when replication target is specified in attached policy. | [optional] 

## Example

```python
from cohesity_sdk.models.common_cdp_params import CommonCdpParams

# TODO update the JSON string below
json = "{}"
# create an instance of CommonCdpParams from a JSON string
common_cdp_params_instance = CommonCdpParams.from_json(json)
# print the JSON string representation of the object
print(CommonCdpParams.to_json())

# convert the object into a dict
common_cdp_params_dict = common_cdp_params_instance.to_dict()
# create an instance of CommonCdpParams from a dict
common_cdp_params_from_dict = CommonCdpParams.from_dict(common_cdp_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


