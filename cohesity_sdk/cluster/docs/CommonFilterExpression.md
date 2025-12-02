# CommonFilterExpression

Specifies the params for filtering an entity. Exactly one of the child objects should be specified for this object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter_policy** | [**CommonFilterPolicy**](CommonFilterPolicy.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.common_filter_expression import CommonFilterExpression

# TODO update the JSON string below
json = "{}"
# create an instance of CommonFilterExpression from a JSON string
common_filter_expression_instance = CommonFilterExpression.from_json(json)
# print the JSON string representation of the object
print(CommonFilterExpression.to_json())

# convert the object into a dict
common_filter_expression_dict = common_filter_expression_instance.to_dict()
# create an instance of CommonFilterExpression from a dict
common_filter_expression_from_dict = CommonFilterExpression.from_dict(common_filter_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


