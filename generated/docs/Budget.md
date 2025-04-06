# Budget


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**name** | **str** |  | 
**active** | **bool** |  | [optional] 
**notes** | **str** |  | [optional] 
**order** | **int** |  | [optional] [readonly] 
**auto_budget_type** | [**AutoBudgetType**](AutoBudgetType.md) |  | [optional] 
**currency_id** | **str** | The currency ID that is part of the budget&#39;s auto-budget settings, if any. | [optional] 
**currency_code** | **str** | The currency code that is part of the budget&#39;s auto-budget settings, if any. | [optional] 
**currency_symbol** | **str** | The currency symbol that is part of the budget&#39;s auto-budget settings, if any. | [optional] [readonly] 
**currency_decimal_places** | **int** | The currency decimal places that is part of the budget&#39;s auto-budget settings, if any. | [optional] [readonly] 
**native_currency_id** | **str** | The administration&#39;s native currency ID. | [optional] [readonly] 
**native_currency_code** | **str** | The administration&#39;s native currency code. | [optional] [readonly] 
**native_currency_symbol** | **str** | The administration&#39;s native currency symbol. | [optional] [readonly] 
**native_currency_decimal_places** | **int** | The administration&#39;s native currency decimal places. | [optional] [readonly] 
**auto_budget_amount** | **str** | The amount for the auto-budget, if set. | [optional] 
**native_auto_budget_amount** | **str** | The native amount for the auto-budget, if set. | [optional] 
**auto_budget_period** | [**AutoBudgetPeriod**](AutoBudgetPeriod.md) |  | [optional] 
**spent** | [**List[BudgetSpent]**](BudgetSpent.md) | Information on how much was spent in this budget. Is only filled in when the start and end date are submitted. | [optional] [readonly] 

## Example

```python
from openapi_client.models.budget import Budget

# TODO update the JSON string below
json = "{}"
# create an instance of Budget from a JSON string
budget_instance = Budget.from_json(json)
# print the JSON string representation of the object
print(Budget.to_json())

# convert the object into a dict
budget_dict = budget_instance.to_dict()
# create an instance of Budget from a dict
budget_from_dict = Budget.from_dict(budget_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


