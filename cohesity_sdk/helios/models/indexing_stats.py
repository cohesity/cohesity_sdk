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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing import Set
from typing_extensions import Self

class IndexingStats(BaseModel):
    """
    Metric related to file indexes.
    """ # noqa: E501
    deleted_document_count: Optional[StrictInt] = Field(default=None, description="Specifies the number of files deleted for this run.", alias="deletedDocumentCount")
    new_document_count: Optional[StrictInt] = Field(default=None, description="Specifies the number of files added for this run.", alias="newDocumentCount")
    not_updated_document_count: Optional[StrictInt] = Field(default=None, description="Specifies the number of files not updated for this run.", alias="notUpdatedDocumentCount")
    total_files: Optional[StrictInt] = Field(default=None, description="Specifies the count of files in this run.", alias="totalFiles")
    updated_document_count: Optional[StrictInt] = Field(default=None, description="Specifies the number of files updated for this run.", alias="updatedDocumentCount")
    __properties: ClassVar[List[str]] = ["deletedDocumentCount", "newDocumentCount", "notUpdatedDocumentCount", "totalFiles", "updatedDocumentCount"]

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
        """Create an instance of IndexingStats from a JSON string"""
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
        # set to None if deleted_document_count (nullable) is None
        # and model_fields_set contains the field
        if self.deleted_document_count is None and "deleted_document_count" in self.model_fields_set:
            _dict['deletedDocumentCount'] = None

        # set to None if new_document_count (nullable) is None
        # and model_fields_set contains the field
        if self.new_document_count is None and "new_document_count" in self.model_fields_set:
            _dict['newDocumentCount'] = None

        # set to None if not_updated_document_count (nullable) is None
        # and model_fields_set contains the field
        if self.not_updated_document_count is None and "not_updated_document_count" in self.model_fields_set:
            _dict['notUpdatedDocumentCount'] = None

        # set to None if total_files (nullable) is None
        # and model_fields_set contains the field
        if self.total_files is None and "total_files" in self.model_fields_set:
            _dict['totalFiles'] = None

        # set to None if updated_document_count (nullable) is None
        # and model_fields_set contains the field
        if self.updated_document_count is None and "updated_document_count" in self.model_fields_set:
            _dict['updatedDocumentCount'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IndexingStats from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "deletedDocumentCount": obj.get("deletedDocumentCount"),
            "newDocumentCount": obj.get("newDocumentCount"),
            "notUpdatedDocumentCount": obj.get("notUpdatedDocumentCount"),
            "totalFiles": obj.get("totalFiles"),
            "updatedDocumentCount": obj.get("updatedDocumentCount")
        })
        return _obj


