# PolicyTemplatesResponseWithPagination

Specifies the details about the Protection Policy Templates.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policies** | [**List[PolicyTemplateResponse]**](PolicyTemplateResponse.md) | Specifies a list of protection policies. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.policy_templates_response_with_pagination import PolicyTemplatesResponseWithPagination

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyTemplatesResponseWithPagination from a JSON string
policy_templates_response_with_pagination_instance = PolicyTemplatesResponseWithPagination.from_json(json)
# print the JSON string representation of the object
print(PolicyTemplatesResponseWithPagination.to_json())

# convert the object into a dict
policy_templates_response_with_pagination_dict = policy_templates_response_with_pagination_instance.to_dict()
# create an instance of PolicyTemplatesResponseWithPagination from a dict
policy_templates_response_with_pagination_from_dict = PolicyTemplatesResponseWithPagination.from_dict(policy_templates_response_with_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


