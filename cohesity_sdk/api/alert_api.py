# coding: utf-8

"""
    Cohesity REST API

    Cohesity API provides a RESTful interface to access the various data management operations on Cohesity cluster and Helios.

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from pydantic import Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import List, Optional
from typing_extensions import Annotated
from cohesity_sdk.models.alerts_summary_response import AlertsSummaryResponse

from cohesity_sdk.api_client import ApiClient, RequestSerialized
from cohesity_sdk.api_response import ApiResponse
from cohesity_sdk.rest import RESTResponseType


class AlertApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def get_alert_summary(
        self,
        start_time_usecs: Annotated[Optional[StrictInt], Field(description="Filter by start time. Specify the start time as a Unix epoch Timestamp (in microseconds). By default it is current time minus a day.")] = None,
        end_time_usecs: Annotated[Optional[StrictInt], Field(description="Filter by end time. Specify the end time as a Unix epoch Timestamp (in microseconds). By default it is current time.")] = None,
        include_tenants: Annotated[Optional[StrictBool], Field(description="IncludeTenants specifies if alerts of all the tenants under the hierarchy of the logged in user's organization should be used to compute summary.")] = None,
        tenant_ids: Annotated[Optional[List[StrictStr]], Field(description="TenantIds contains ids of the tenants for which alerts are to be used to compute summary.")] = None,
        states_list: Annotated[Optional[List[StrictStr]], Field(description="Specifies list of alert states to filter alerts by. If not specified, only open alerts will be used to get summary.")] = None,
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
    ) -> AlertsSummaryResponse:
        """Get alerts summary.

        Get alerts summary grouped by category.

        :param start_time_usecs: Filter by start time. Specify the start time as a Unix epoch Timestamp (in microseconds). By default it is current time minus a day.
        :type start_time_usecs: int
        :param end_time_usecs: Filter by end time. Specify the end time as a Unix epoch Timestamp (in microseconds). By default it is current time.
        :type end_time_usecs: int
        :param include_tenants: IncludeTenants specifies if alerts of all the tenants under the hierarchy of the logged in user's organization should be used to compute summary.
        :type include_tenants: bool
        :param tenant_ids: TenantIds contains ids of the tenants for which alerts are to be used to compute summary.
        :type tenant_ids: List[str]
        :param states_list: Specifies list of alert states to filter alerts by. If not specified, only open alerts will be used to get summary.
        :type states_list: List[str]
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

        _param = self._get_alert_summary_serialize(
            start_time_usecs=start_time_usecs,
            end_time_usecs=end_time_usecs,
            include_tenants=include_tenants,
            tenant_ids=tenant_ids,
            states_list=states_list,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AlertsSummaryResponse",
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
    def get_alert_summary_with_http_info(
        self,
        start_time_usecs: Annotated[Optional[StrictInt], Field(description="Filter by start time. Specify the start time as a Unix epoch Timestamp (in microseconds). By default it is current time minus a day.")] = None,
        end_time_usecs: Annotated[Optional[StrictInt], Field(description="Filter by end time. Specify the end time as a Unix epoch Timestamp (in microseconds). By default it is current time.")] = None,
        include_tenants: Annotated[Optional[StrictBool], Field(description="IncludeTenants specifies if alerts of all the tenants under the hierarchy of the logged in user's organization should be used to compute summary.")] = None,
        tenant_ids: Annotated[Optional[List[StrictStr]], Field(description="TenantIds contains ids of the tenants for which alerts are to be used to compute summary.")] = None,
        states_list: Annotated[Optional[List[StrictStr]], Field(description="Specifies list of alert states to filter alerts by. If not specified, only open alerts will be used to get summary.")] = None,
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
    ) -> ApiResponse[AlertsSummaryResponse]:
        """Get alerts summary.

        Get alerts summary grouped by category.

        :param start_time_usecs: Filter by start time. Specify the start time as a Unix epoch Timestamp (in microseconds). By default it is current time minus a day.
        :type start_time_usecs: int
        :param end_time_usecs: Filter by end time. Specify the end time as a Unix epoch Timestamp (in microseconds). By default it is current time.
        :type end_time_usecs: int
        :param include_tenants: IncludeTenants specifies if alerts of all the tenants under the hierarchy of the logged in user's organization should be used to compute summary.
        :type include_tenants: bool
        :param tenant_ids: TenantIds contains ids of the tenants for which alerts are to be used to compute summary.
        :type tenant_ids: List[str]
        :param states_list: Specifies list of alert states to filter alerts by. If not specified, only open alerts will be used to get summary.
        :type states_list: List[str]
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

        _param = self._get_alert_summary_serialize(
            start_time_usecs=start_time_usecs,
            end_time_usecs=end_time_usecs,
            include_tenants=include_tenants,
            tenant_ids=tenant_ids,
            states_list=states_list,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AlertsSummaryResponse",
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
    def get_alert_summary_without_preload_content(
        self,
        start_time_usecs: Annotated[Optional[StrictInt], Field(description="Filter by start time. Specify the start time as a Unix epoch Timestamp (in microseconds). By default it is current time minus a day.")] = None,
        end_time_usecs: Annotated[Optional[StrictInt], Field(description="Filter by end time. Specify the end time as a Unix epoch Timestamp (in microseconds). By default it is current time.")] = None,
        include_tenants: Annotated[Optional[StrictBool], Field(description="IncludeTenants specifies if alerts of all the tenants under the hierarchy of the logged in user's organization should be used to compute summary.")] = None,
        tenant_ids: Annotated[Optional[List[StrictStr]], Field(description="TenantIds contains ids of the tenants for which alerts are to be used to compute summary.")] = None,
        states_list: Annotated[Optional[List[StrictStr]], Field(description="Specifies list of alert states to filter alerts by. If not specified, only open alerts will be used to get summary.")] = None,
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
        """Get alerts summary.

        Get alerts summary grouped by category.

        :param start_time_usecs: Filter by start time. Specify the start time as a Unix epoch Timestamp (in microseconds). By default it is current time minus a day.
        :type start_time_usecs: int
        :param end_time_usecs: Filter by end time. Specify the end time as a Unix epoch Timestamp (in microseconds). By default it is current time.
        :type end_time_usecs: int
        :param include_tenants: IncludeTenants specifies if alerts of all the tenants under the hierarchy of the logged in user's organization should be used to compute summary.
        :type include_tenants: bool
        :param tenant_ids: TenantIds contains ids of the tenants for which alerts are to be used to compute summary.
        :type tenant_ids: List[str]
        :param states_list: Specifies list of alert states to filter alerts by. If not specified, only open alerts will be used to get summary.
        :type states_list: List[str]
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

        _param = self._get_alert_summary_serialize(
            start_time_usecs=start_time_usecs,
            end_time_usecs=end_time_usecs,
            include_tenants=include_tenants,
            tenant_ids=tenant_ids,
            states_list=states_list,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AlertsSummaryResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_alert_summary_serialize(
        self,
        start_time_usecs,
        end_time_usecs,
        include_tenants,
        tenant_ids,
        states_list,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'tenantIds': 'csv',
            'statesList': 'csv',
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
        if start_time_usecs is not None:
            
            _query_params.append(('startTimeUsecs', start_time_usecs))
            
        if end_time_usecs is not None:
            
            _query_params.append(('endTimeUsecs', end_time_usecs))
            
        if include_tenants is not None:
            
            _query_params.append(('includeTenants', include_tenants))
            
        if tenant_ids is not None:
            
            _query_params.append(('tenantIds', tenant_ids))
            
        if states_list is not None:
            
            _query_params.append(('statesList', states_list))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'APIKeyHeader', 
            'Bearer'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/alerts-summary',
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


