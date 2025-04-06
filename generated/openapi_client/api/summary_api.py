# coding: utf-8

"""
    Firefly III API v6.2.9

    This is the documentation of the Firefly III API. You can find accompanying documentation on the website of Firefly III itself (see below). Please report any bugs or issues. You may use the \"Authorize\" button to try the API below. This file was last generated on 2025-03-05T19:12:52+00:00 Please keep in mind that the demo site does not accept requests from curl, colly, wget, etc. You must use a browser or a tool like Postman to make requests. Too many script kiddies out there, sorry about that. 

    The version of the OpenAPI document: v6.2.9
    Contact: james@firefly-iii.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from datetime import date
from pydantic import Field, StrictStr
from typing import Dict, Optional
from typing_extensions import Annotated
from openapi_client.models.basic_summary_entry import BasicSummaryEntry

from openapi_client.api_client import ApiClient, RequestSerialized
from openapi_client.api_response import ApiResponse
from openapi_client.rest import RESTResponseType


class SummaryApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def get_basic_summary(
        self,
        start: Annotated[date, Field(description="A date formatted YYYY-MM-DD. ")],
        end: Annotated[date, Field(description="A date formatted YYYY-MM-DD. ")],
        x_trace_id: Annotated[Optional[StrictStr], Field(description="Unique identifier associated with this request.")] = None,
        currency_code: Annotated[Optional[StrictStr], Field(description="A currency code like EUR or USD, to filter the result. ")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> Dict[str, BasicSummaryEntry]:
        """Returns basic sums of the users data.

        Returns basic sums of the users data, like the net worth, spent and earned amounts. It is multi-currency, and is used in Firefly III to populate the dashboard. 

        :param start: A date formatted YYYY-MM-DD.  (required)
        :type start: date
        :param end: A date formatted YYYY-MM-DD.  (required)
        :type end: date
        :param x_trace_id: Unique identifier associated with this request.
        :type x_trace_id: str
        :param currency_code: A currency code like EUR or USD, to filter the result. 
        :type currency_code: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_basic_summary_serialize(
            start=start,
            end=end,
            x_trace_id=x_trace_id,
            currency_code=currency_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Dict[str, BasicSummaryEntry]",
            '401': "UnauthenticatedResponse",
            '404': "NotFoundResponse",
            '400': "BadRequestResponse",
            '500': "InternalExceptionResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def get_basic_summary_with_http_info(
        self,
        start: Annotated[date, Field(description="A date formatted YYYY-MM-DD. ")],
        end: Annotated[date, Field(description="A date formatted YYYY-MM-DD. ")],
        x_trace_id: Annotated[Optional[StrictStr], Field(description="Unique identifier associated with this request.")] = None,
        currency_code: Annotated[Optional[StrictStr], Field(description="A currency code like EUR or USD, to filter the result. ")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[Dict[str, BasicSummaryEntry]]:
        """Returns basic sums of the users data.

        Returns basic sums of the users data, like the net worth, spent and earned amounts. It is multi-currency, and is used in Firefly III to populate the dashboard. 

        :param start: A date formatted YYYY-MM-DD.  (required)
        :type start: date
        :param end: A date formatted YYYY-MM-DD.  (required)
        :type end: date
        :param x_trace_id: Unique identifier associated with this request.
        :type x_trace_id: str
        :param currency_code: A currency code like EUR or USD, to filter the result. 
        :type currency_code: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_basic_summary_serialize(
            start=start,
            end=end,
            x_trace_id=x_trace_id,
            currency_code=currency_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Dict[str, BasicSummaryEntry]",
            '401': "UnauthenticatedResponse",
            '404': "NotFoundResponse",
            '400': "BadRequestResponse",
            '500': "InternalExceptionResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def get_basic_summary_without_preload_content(
        self,
        start: Annotated[date, Field(description="A date formatted YYYY-MM-DD. ")],
        end: Annotated[date, Field(description="A date formatted YYYY-MM-DD. ")],
        x_trace_id: Annotated[Optional[StrictStr], Field(description="Unique identifier associated with this request.")] = None,
        currency_code: Annotated[Optional[StrictStr], Field(description="A currency code like EUR or USD, to filter the result. ")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Returns basic sums of the users data.

        Returns basic sums of the users data, like the net worth, spent and earned amounts. It is multi-currency, and is used in Firefly III to populate the dashboard. 

        :param start: A date formatted YYYY-MM-DD.  (required)
        :type start: date
        :param end: A date formatted YYYY-MM-DD.  (required)
        :type end: date
        :param x_trace_id: Unique identifier associated with this request.
        :type x_trace_id: str
        :param currency_code: A currency code like EUR or USD, to filter the result. 
        :type currency_code: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_basic_summary_serialize(
            start=start,
            end=end,
            x_trace_id=x_trace_id,
            currency_code=currency_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Dict[str, BasicSummaryEntry]",
            '401': "UnauthenticatedResponse",
            '404': "NotFoundResponse",
            '400': "BadRequestResponse",
            '500': "InternalExceptionResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_basic_summary_serialize(
        self,
        start,
        end,
        x_trace_id,
        currency_code,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if start is not None:
            if isinstance(start, date):
                _query_params.append(
                    (
                        'start',
                        start.strftime(
                            self.api_client.configuration.date_format
                        )
                    )
                )
            else:
                _query_params.append(('start', start))
            
        if end is not None:
            if isinstance(end, date):
                _query_params.append(
                    (
                        'end',
                        end.strftime(
                            self.api_client.configuration.date_format
                        )
                    )
                )
            else:
                _query_params.append(('end', end))
            
        if currency_code is not None:
            
            _query_params.append(('currency_code', currency_code))
            
        # process the header parameters
        if x_trace_id is not None:
            _header_params['X-Trace-Id'] = x_trace_id
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/vnd.api+json', 
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'firefly_iii_auth', 
            'local_bearer_auth'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/v1/summary/basic',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


