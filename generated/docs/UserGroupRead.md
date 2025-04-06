# UserGroupRead


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Immutable value | 
**id** | **str** |  | 
**attributes** | [**UserGroupReadAttributes**](UserGroupReadAttributes.md) |  | 
**links** | [**ObjectLink**](ObjectLink.md) |  | 

## Example

```python
from openapi_client.models.user_group_read import UserGroupRead

# TODO update the JSON string below
json = "{}"
# create an instance of UserGroupRead from a JSON string
user_group_read_instance = UserGroupRead.from_json(json)
# print the JSON string representation of the object
print(UserGroupRead.to_json())

# convert the object into a dict
user_group_read_dict = user_group_read_instance.to_dict()
# create an instance of UserGroupRead from a dict
user_group_read_from_dict = UserGroupRead.from_dict(user_group_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


