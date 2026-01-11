# SearchGraphNodesRequestParamsAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_id** | **str** | Specifies the id of a Session. | 
**count** | **int** | Specifies the number of graph nodes to be fetched for the specified pagination cookie. | [optional] 
**include_attributes** | **bool, none_type** | If set to false the response will only return name, type and is_root fields filled in each node. If set to true all the attributes for the nodes are also returned. Defaults to true. | [optional] 
**pagination_cookie** | **str, none_type** | Specifies a cookie which can be passed in by the user in order to retrieve the next page of results. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


