# TagRead


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Immutable value | 
**id** | **str** |  | 
**attributes** | [**TagModel**](TagModel.md) |  | 
**links** | [**ObjectLink**](ObjectLink.md) |  | 

## Example

```python
from openapi_client.models.tag_read import TagRead

# TODO update the JSON string below
json = "{}"
# create an instance of TagRead from a JSON string
tag_read_instance = TagRead.from_json(json)
# print the JSON string representation of the object
print(TagRead.to_json())

# convert the object into a dict
tag_read_dict = tag_read_instance.to_dict()
# create an instance of TagRead from a dict
tag_read_from_dict = TagRead.from_dict(tag_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


