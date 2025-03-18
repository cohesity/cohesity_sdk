# DSESolrInfo

Contains details about DSE Solr.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**solr_nodes** | **List[str]** | Solr node IP Addresses | 
**solr_port** | **int** | Solr node Port. | 

## Example

```python
from cohesity_sdk.cluster.models.dse_solr_info import DSESolrInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DSESolrInfo from a JSON string
dse_solr_info_instance = DSESolrInfo.from_json(json)
# print the JSON string representation of the object
print(DSESolrInfo.to_json())

# convert the object into a dict
dse_solr_info_dict = dse_solr_info_instance.to_dict()
# create an instance of DSESolrInfo from a dict
dse_solr_info_from_dict = DSESolrInfo.from_dict(dse_solr_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


