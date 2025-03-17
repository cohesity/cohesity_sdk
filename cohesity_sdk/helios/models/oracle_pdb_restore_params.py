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

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.helios.models.key_value_pair import KeyValuePair
from cohesity_sdk.helios.models.oracle_pdb_object_info import OraclePdbObjectInfo
from typing import Set
from typing_extensions import Self

class OraclePdbRestoreParams(BaseModel):
    """
    Specifies information about the list of pdbs to be restored.
    """ # noqa: E501
    drop_duplicate_pdb: Optional[StrictBool] = Field(default=None, description="Specifies if the PDB should be ignored if a PDB already exists with same name.", alias="dropDuplicatePDB")
    include_in_restore: Optional[StrictBool] = Field(default=None, description="Specifies whether to restore or skip the provided PDBs list.", alias="includeInRestore")
    pdb_objects: Optional[List[OraclePdbObjectInfo]] = Field(default=None, description="Specifies list of PDB objects to restore.", alias="pdbObjects")
    rename_pdb_map: Optional[List[KeyValuePair]] = Field(default=None, description="Specifies the new PDB name mapping to existing PDBs.", alias="renamePdbMap")
    restore_to_existing_cdb: Optional[StrictBool] = Field(default=None, description="Specifies if pdbs should be restored to an existing CDB.", alias="restoreToExistingCdb")
    __properties: ClassVar[List[str]] = ["dropDuplicatePDB", "includeInRestore", "pdbObjects", "renamePdbMap", "restoreToExistingCdb"]

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
        """Create an instance of OraclePdbRestoreParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in pdb_objects (list)
        _items = []
        if self.pdb_objects:
            for _item_pdb_objects in self.pdb_objects:
                if _item_pdb_objects:
                    _items.append(_item_pdb_objects.to_dict())
            _dict['pdbObjects'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in rename_pdb_map (list)
        _items = []
        if self.rename_pdb_map:
            for _item_rename_pdb_map in self.rename_pdb_map:
                if _item_rename_pdb_map:
                    _items.append(_item_rename_pdb_map.to_dict())
            _dict['renamePdbMap'] = _items
        # set to None if drop_duplicate_pdb (nullable) is None
        # and model_fields_set contains the field
        if self.drop_duplicate_pdb is None and "drop_duplicate_pdb" in self.model_fields_set:
            _dict['dropDuplicatePDB'] = None

        # set to None if include_in_restore (nullable) is None
        # and model_fields_set contains the field
        if self.include_in_restore is None and "include_in_restore" in self.model_fields_set:
            _dict['includeInRestore'] = None

        # set to None if pdb_objects (nullable) is None
        # and model_fields_set contains the field
        if self.pdb_objects is None and "pdb_objects" in self.model_fields_set:
            _dict['pdbObjects'] = None

        # set to None if rename_pdb_map (nullable) is None
        # and model_fields_set contains the field
        if self.rename_pdb_map is None and "rename_pdb_map" in self.model_fields_set:
            _dict['renamePdbMap'] = None

        # set to None if restore_to_existing_cdb (nullable) is None
        # and model_fields_set contains the field
        if self.restore_to_existing_cdb is None and "restore_to_existing_cdb" in self.model_fields_set:
            _dict['restoreToExistingCdb'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OraclePdbRestoreParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "dropDuplicatePDB": obj.get("dropDuplicatePDB"),
            "includeInRestore": obj.get("includeInRestore"),
            "pdbObjects": [OraclePdbObjectInfo.from_dict(_item) for _item in obj["pdbObjects"]] if obj.get("pdbObjects") is not None else None,
            "renamePdbMap": [KeyValuePair.from_dict(_item) for _item in obj["renamePdbMap"]] if obj.get("renamePdbMap") is not None else None,
            "restoreToExistingCdb": obj.get("restoreToExistingCdb")
        })
        return _obj


