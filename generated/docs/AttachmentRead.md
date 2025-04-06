# AttachmentRead


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Immutable value | 
**id** | **str** |  | 
**attributes** | [**Attachment**](Attachment.md) |  | 
**links** | [**ObjectLink**](ObjectLink.md) |  | 

## Example

```python
from openapi_client.models.attachment_read import AttachmentRead

# TODO update the JSON string below
json = "{}"
# create an instance of AttachmentRead from a JSON string
attachment_read_instance = AttachmentRead.from_json(json)
# print the JSON string representation of the object
print(AttachmentRead.to_json())

# convert the object into a dict
attachment_read_dict = attachment_read_instance.to_dict()
# create an instance of AttachmentRead from a dict
attachment_read_from_dict = AttachmentRead.from_dict(attachment_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


