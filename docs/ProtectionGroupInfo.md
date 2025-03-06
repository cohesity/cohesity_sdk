# ProtectionGroupInfo

Specifies basic information about a Protection Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **int** | This field is deprecated. &#39;protectionGroupId&#39; should be used instead. Specifies the id of the Protection Group. | [optional] 
**group_name** | **str** | Specifies the name of the Protection Group. | [optional] 
**is_paused** | **bool** | Specifies if the Protection Group&#39;s run is paused. | [optional] 
**last_run** | [**CommonProtectionGroupRunResponseParameters**](CommonProtectionGroupRunResponseParameters.md) |  | [optional] 
**protection_group_id** | **str** | Specifies the protection group id. | [optional] 
**type** | **str** | Specifies the type of the Protection Group such as View or Puppeteer. &#39;Puppeteer&#39; refers to a Remote Adapter Group. Supported environment types such as &#39;View&#39;, &#39;SQL&#39;, &#39;VMware&#39;, etc. NOTE: &#39;Puppeteer&#39; refers to Cohesity&#39;s Remote Adapter. &#39;VMware&#39; indicates the VMware Protection Source environment. &#39;HyperV&#39; indicates the HyperV Protection Source environment. &#39;SQL&#39; indicates the SQL Protection Source environment. &#39;View&#39; indicates the View Protection Source environment. &#39;Puppeteer&#39; indicates the Cohesity&#39;s Remote Adapter. &#39;Physical&#39; indicates the physical Protection Source environment. &#39;Pure&#39; indicates the Pure Storage Protection Source environment. &#39;Nimble&#39; indicates the Nimble Storage Protection Source environment. &#39;Azure&#39; indicates the Microsoft&#39;s Azure Protection Source environment. &#39;Netapp&#39; indicates the Netapp Protection Source environment. &#39;Agent&#39; indicates the Agent Protection Source environment. &#39;GenericNas&#39; indicates the Generic Network Attached Storage Protection Source environment. &#39;Acropolis&#39; indicates the Acropolis Protection Source environment. &#39;PhsicalFiles&#39; indicates the Physical Files Protection Source environment. &#39;Isilon&#39; indicates the Dell EMC&#39;s Isilon Protection Source environment. &#39;GPFS&#39; indicates IBM&#39;s GPFS Protection Source environment. &#39;KVM&#39; indicates the KVM Protection Source environment. &#39;AWS&#39; indicates the AWS Protection Source environment. &#39;Exchange&#39; indicates the Exchange Protection Source environment. &#39;HyperVVSS&#39; indicates the HyperV VSS Protection Source environment. &#39;Oracle&#39; indicates the Oracle Protection Source environment. &#39;GCP&#39; indicates the Google Cloud Platform Protection Source environment. &#39;FlashBlade&#39; indicates the Flash Blade Protection Source environment. &#39;AWSNative&#39; indicates the AWS Native Protection Source environment. &#39;O365&#39; indicates the Office 365 Protection Source environment. &#39;O365Outlook&#39; indicates Office 365 outlook Protection Source environment. &#39;HyperFlex&#39; indicates the Hyper Flex Protection Source environment. &#39;GCPNative&#39; indicates the GCP Native Protection Source environment. &#39;AzureNative&#39; indicates the Azure Native Protection Source environment. &#39;Kubernetes&#39; indicates a Kubernetes Protection Source environment. &#39;Elastifile&#39; indicates Elastifile Protection Source environment. &#39;AD&#39; indicates Active Directory Protection Source environment. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.protection_group_info import ProtectionGroupInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ProtectionGroupInfo from a JSON string
protection_group_info_instance = ProtectionGroupInfo.from_json(json)
# print the JSON string representation of the object
print(ProtectionGroupInfo.to_json())

# convert the object into a dict
protection_group_info_dict = protection_group_info_instance.to_dict()
# create an instance of ProtectionGroupInfo from a dict
protection_group_info_from_dict = ProtectionGroupInfo.from_dict(protection_group_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


