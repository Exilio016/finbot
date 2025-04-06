# RecurrenceStore


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**RecurrenceTransactionType**](RecurrenceTransactionType.md) |  | 
**title** | **str** |  | 
**description** | **str** | Not to be confused with the description of the actual transaction(s) being created. | [optional] 
**first_date** | **date** | First time the recurring transaction will fire. Must be after today. | 
**repeat_until** | **date** | Date until the recurring transaction can fire. Use either this field or repetitions. | 
**nr_of_repetitions** | **int** | Max number of created transactions. Use either this field or repeat_until. | [optional] 
**apply_rules** | **bool** | Whether or not to fire the rules after the creation of a transaction. | [optional] 
**active** | **bool** | If the recurrence is even active. | [optional] 
**notes** | **str** |  | [optional] 
**repetitions** | [**List[RecurrenceRepetitionStore]**](RecurrenceRepetitionStore.md) |  | 
**transactions** | [**List[RecurrenceTransactionStore]**](RecurrenceTransactionStore.md) |  | 

## Example

```python
from openapi_client.models.recurrence_store import RecurrenceStore

# TODO update the JSON string below
json = "{}"
# create an instance of RecurrenceStore from a JSON string
recurrence_store_instance = RecurrenceStore.from_json(json)
# print the JSON string representation of the object
print(RecurrenceStore.to_json())

# convert the object into a dict
recurrence_store_dict = recurrence_store_instance.to_dict()
# create an instance of RecurrenceStore from a dict
recurrence_store_from_dict = RecurrenceStore.from_dict(recurrence_store_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


