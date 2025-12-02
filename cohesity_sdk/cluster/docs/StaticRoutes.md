# StaticRoutes

Specifies a list of defined static routes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**routes** | [**List[StaticRouteParams]**](StaticRouteParams.md) | Specifies the list of routes. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.static_routes import StaticRoutes

# TODO update the JSON string below
json = "{}"
# create an instance of StaticRoutes from a JSON string
static_routes_instance = StaticRoutes.from_json(json)
# print the JSON string representation of the object
print(StaticRoutes.to_json())

# convert the object into a dict
static_routes_dict = static_routes_instance.to_dict()
# create an instance of StaticRoutes from a dict
static_routes_from_dict = StaticRoutes.from_dict(static_routes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


