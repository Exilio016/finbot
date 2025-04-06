# Recurrence


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**type** | [**RecurrenceTransactionType**](RecurrenceTransactionType.md) |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** | Not to be confused with the description of the actual transaction(s) being created. | [optional] 
**first_date** | **date** | First time the recurring transaction will fire. Must be after today. | [optional] 
**latest_date** | **date** | Last time the recurring transaction has fired. | [optional] [readonly] 
**repeat_until** | **date** | Date until the recurring transaction can fire. Use either this field or repetitions. | [optional] 
**nr_of_repetitions** | **int** | Max number of created transactions. Use either this field or repeat_until. | [optional] 
**apply_rules** | **bool** | Whether or not to fire the rules after the creation of a transaction. | [optional] 
**active** | **bool** | If the recurrence is even active. | [optional] 
**notes** | **str** |  | [optional] 
**repetitions** | [**List[RecurrenceRepetition]**](RecurrenceRepetition.md) |  | [optional] 
**transactions** | [**List[RecurrenceTransaction]**](RecurrenceTransaction.md) |  | [optional] 

## Example

```python
from openapi_client.models.recurrence import Recurrence

# TODO update the JSON string below
json = "{}"
# create an instance of Recurrence from a JSON string
recurrence_instance = Recurrence.from_json(json)
# print the JSON string representation of the object
print(Recurrence.to_json())

# convert the object into a dict
recurrence_dict = recurrence_instance.to_dict()
# create an instance of Recurrence from a dict
recurrence_from_dict = Recurrence.from_dict(recurrence_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


