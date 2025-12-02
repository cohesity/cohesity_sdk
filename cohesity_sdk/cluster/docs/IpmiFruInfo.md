# IpmiFruInfo

Specifies the fru for the ipmi.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the IPMI Field Replaceable Unit(FRU) ID for given node. | [optional] 
**board_mfg** | **str** | Specifies the board manufacturer for given node. | [optional] 
**board_mfg_date** | **str** | Specifies the board manufacturing date for given node. | [optional] 
**board_pn** | **str** | Specifies the board part number for given node. | [optional] 
**board_product** | **str** | Specifies the board product name for given node. | [optional] 
**board_serial** | **str** | Specifies the board serial number for given node. | [optional] 
**chassis_extra** | **str** | Specifies the information about chassis extras provided for given node. | [optional] 
**chassis_pn** | **str** | Specifies the chassis part number for given node. | [optional] 
**chassis_serial** | **str** | Specifies the chassis serial number for given node. | [optional] 
**chassis_type** | **str** | Specifies the type of chassis for given node. | [optional] 
**product_mfg** | **str** | Specifies the product manufacturer for given node. | [optional] 
**product_name** | **str** | Specifies the product name for given node. | [optional] 
**product_pn** | **str** | Specifies the product part number for given node. | [optional] 
**product_serial** | **str** | Specifies the product serial number for given node. | [optional] 
**product_version** | **str** | Specifies the product version for given node. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.ipmi_fru_info import IpmiFruInfo

# TODO update the JSON string below
json = "{}"
# create an instance of IpmiFruInfo from a JSON string
ipmi_fru_info_instance = IpmiFruInfo.from_json(json)
# print the JSON string representation of the object
print(IpmiFruInfo.to_json())

# convert the object into a dict
ipmi_fru_info_dict = ipmi_fru_info_instance.to_dict()
# create an instance of IpmiFruInfo from a dict
ipmi_fru_info_from_dict = IpmiFruInfo.from_dict(ipmi_fru_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


