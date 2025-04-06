# Attachment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**attachable_type** | [**AttachableType**](AttachableType.md) |  | 
**attachable_id** | **str** | ID of the model this attachment is linked to. | 
**md5** | **str** | MD5 hash of the file for basic duplicate detection. This field is deprecated. | [optional] 
**hash** | **str** | Hash of the file for basic duplicate detection. It&#39;s still md5 lol. | [optional] 
**filename** | **str** |  | 
**download_url** | **str** |  | [optional] 
**upload_url** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**notes** | **str** |  | [optional] 
**mime** | **str** |  | [optional] [readonly] 
**size** | **int** |  | [optional] [readonly] 

## Example

```python
from openapi_client.models.attachment import Attachment

# TODO update the JSON string below
json = "{}"
# create an instance of Attachment from a JSON string
attachment_instance = Attachment.from_json(json)
# print the JSON string representation of the object
print(Attachment.to_json())

# convert the object into a dict
attachment_dict = attachment_instance.to_dict()
# create an instance of Attachment from a dict
attachment_from_dict = Attachment.from_dict(attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


