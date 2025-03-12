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
from cohesity_sdk.helios.models.common_recover_object_snapshot_params import CommonRecoverObjectSnapshotParams
from cohesity_sdk.helios.models.one_drive_param import OneDriveParam
from typing import Optional, Set
from typing_extensions import Self

class ObjectSiteParam(BaseModel):
    """
    Specifies Site recovery parameters.
    """ # noqa: E501
    document_library_params: Optional[List[OneDriveParam]] = Field(default=None, description="Specifies the parameters to recover a document library", alias="documentLibraryParams")
    owner_info: CommonRecoverObjectSnapshotParams = Field(alias="ownerInfo")
    __properties: ClassVar[List[str]] = ["documentLibraryParams", "ownerInfo"]

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
        """Create an instance of ObjectSiteParam from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in document_library_params (list)
        _items = []
        if self.document_library_params:
            for _item_document_library_params in self.document_library_params:
                if _item_document_library_params:
                    _items.append(_item_document_library_params.to_dict())
            _dict['documentLibraryParams'] = _items
        # override the default output from pydantic by calling `to_dict()` of owner_info
        if self.owner_info:
            _dict['ownerInfo'] = self.owner_info.to_dict()
        # set to None if document_library_params (nullable) is None
        # and model_fields_set contains the field
        if self.document_library_params is None and "document_library_params" in self.model_fields_set:
            _dict['documentLibraryParams'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ObjectSiteParam from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "documentLibraryParams": [OneDriveParam.from_dict(_item) for _item in obj["documentLibraryParams"]] if obj.get("documentLibraryParams") is not None else None,
            "ownerInfo": CommonRecoverObjectSnapshotParams.from_dict(obj["ownerInfo"]) if obj.get("ownerInfo") is not None else None
        })
        return _obj


