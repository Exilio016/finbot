# RecurrenceRead


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Immutable value | 
**id** | **str** |  | 
**attributes** | [**Recurrence**](Recurrence.md) |  | 
**links** | [**ObjectLink**](ObjectLink.md) |  | 

## Example

```python
from openapi_client.models.recurrence_read import RecurrenceRead

# TODO update the JSON string below
json = "{}"
# create an instance of RecurrenceRead from a JSON string
recurrence_read_instance = RecurrenceRead.from_json(json)
# print the JSON string representation of the object
print(RecurrenceRead.to_json())

# convert the object into a dict
recurrence_read_dict = recurrence_read_instance.to_dict()
# create an instance of RecurrenceRead from a dict
recurrence_read_from_dict = RecurrenceRead.from_dict(recurrence_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


