# CommonGroupParams

Specifies common group parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Specifies the description of the group. | [optional] 
**domain** | **str** | Specifies the domain of the group. For active directories, this is the fully qualified domain name (FQDN). It is &#39;LOCAL&#39; for local groups on the Cohesity Cluster. A group is uniquely identified by combination of the name and the domain. | 
**group_type** | **str** | Specifies the type of group: local, ad, or idp. | 
**name** | **str** | Specifies the name of the group. | 
**restricted** | **bool** | Specifies whether the Group is restricted. A restricted group can only view &amp; manage the objects it has permissions to. | [optional] 
**roles** | **List[str]** | Specifies the Cohesity roles to associate with the group. The Cohesity roles determine privileges on the Cohesity Cluster for this group. | [optional] 
**tenant_ids** | **List[str]** | Specifies a list of tenant ids who can access this group. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.common_group_params import CommonGroupParams

# TODO update the JSON string below
json = "{}"
# create an instance of CommonGroupParams from a JSON string
common_group_params_instance = CommonGroupParams.from_json(json)
# print the JSON string representation of the object
print(CommonGroupParams.to_json())

# convert the object into a dict
common_group_params_dict = common_group_params_instance.to_dict()
# create an instance of CommonGroupParams from a dict
common_group_params_from_dict = CommonGroupParams.from_dict(common_group_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


