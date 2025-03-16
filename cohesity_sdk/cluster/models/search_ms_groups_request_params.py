# coding: utf-8

"""
    Cohesity REST API

    Cohesity API provides a RESTful interface to access the various data management operations on Cohesity cluster and Helios.

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.cluster.models.o365_search_request_params import O365SearchRequestParams
from cohesity_sdk.cluster.models.search_document_library_request_params import SearchDocumentLibraryRequestParams
from cohesity_sdk.cluster.models.search_email_request_params_base import SearchEmailRequestParamsBase
from typing import Optional, Set
from typing_extensions import Self

class SearchMsGroupsRequestParams(BaseModel):
    """
    Specifies the request params to search for Groups items.
    """ # noqa: E501
    mailbox_params: Optional[SearchEmailRequestParamsBase] = Field(default=None, alias="mailboxParams")
    o365_params: Optional[O365SearchRequestParams] = Field(default=None, alias="o365Params")
    site_params: Optional[SearchDocumentLibraryRequestParams] = Field(default=None, alias="siteParams")
    __properties: ClassVar[List[str]] = ["mailboxParams", "o365Params", "siteParams"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of SearchMsGroupsRequestParams from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of mailbox_params
        if self.mailbox_params:
            _dict['mailboxParams'] = self.mailbox_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of o365_params
        if self.o365_params:
            _dict['o365Params'] = self.o365_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of site_params
        if self.site_params:
            _dict['siteParams'] = self.site_params.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SearchMsGroupsRequestParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "mailboxParams": SearchEmailRequestParamsBase.from_dict(obj["mailboxParams"]) if obj.get("mailboxParams") is not None else None,
            "o365Params": O365SearchRequestParams.from_dict(obj["o365Params"]) if obj.get("o365Params") is not None else None,
            "siteParams": SearchDocumentLibraryRequestParams.from_dict(obj["siteParams"]) if obj.get("siteParams") is not None else None
        })
        return _obj


