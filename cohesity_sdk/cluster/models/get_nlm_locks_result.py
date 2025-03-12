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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.cluster.models.file_nlm_locks import FileNlmLocks
from typing import Set
from typing_extensions import Self

class GetNlmLocksResult(BaseModel):
    """
    Specifies the list of NLM locks.
    """ # noqa: E501
    cookie: Optional[StrictStr] = Field(default=None, description="Specifies the pagination cookie.")
    file_nlm_locks: Optional[List[FileNlmLocks]] = Field(default=None, description="Specifies the list of NLM locks.", alias="fileNlmLocks")
    __properties: ClassVar[List[str]] = ["cookie", "fileNlmLocks"]

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
        """Create an instance of GetNlmLocksResult from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in file_nlm_locks (list)
        _items = []
        if self.file_nlm_locks:
            for _item_file_nlm_locks in self.file_nlm_locks:
                if _item_file_nlm_locks:
                    _items.append(_item_file_nlm_locks.to_dict())
            _dict['fileNlmLocks'] = _items
        # set to None if cookie (nullable) is None
        # and model_fields_set contains the field
        if self.cookie is None and "cookie" in self.model_fields_set:
            _dict['cookie'] = None

        # set to None if file_nlm_locks (nullable) is None
        # and model_fields_set contains the field
        if self.file_nlm_locks is None and "file_nlm_locks" in self.model_fields_set:
            _dict['fileNlmLocks'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetNlmLocksResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "cookie": obj.get("cookie"),
            "fileNlmLocks": [FileNlmLocks.from_dict(_item) for _item in obj["fileNlmLocks"]] if obj.get("fileNlmLocks") is not None else None
        })
        return _obj


