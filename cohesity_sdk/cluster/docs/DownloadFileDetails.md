# DownloadFileDetails

Specifies the details of a file to be downloaded.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_message** | **str** | Specifies error message about the file download. | [optional] 
**file_path** | **str** |  | [optional] 
**identifier** | **str** |  | [optional] 
**progress_task_id** | **str** | Progress monitor task id for download of file. | [optional] 
**status** | **str** | Status of the file download. &#39;Running&#39; indicates that the Download is still running. &#39;Canceled&#39; indicates that the Download has been cancelled. &#39;Failed&#39; indicates that the Download has failed. &#39;Succeeded&#39; indicates that the Download has finished successfully. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.download_file_details import DownloadFileDetails

# TODO update the JSON string below
json = "{}"
# create an instance of DownloadFileDetails from a JSON string
download_file_details_instance = DownloadFileDetails.from_json(json)
# print the JSON string representation of the object
print(DownloadFileDetails.to_json())

# convert the object into a dict
download_file_details_dict = download_file_details_instance.to_dict()
# create an instance of DownloadFileDetails from a dict
download_file_details_from_dict = DownloadFileDetails.from_dict(download_file_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


