#!/usr/bin/env python3
"""Preprocess script for find-CBaseModelEntity_RegisteredScriptFuncs skill."""

from ida_analyze_util import preprocess_common_skill

TARGET_FUNCTION_NAMES = [
    "CBaseModelEntity_GetModelScale",
    "CBaseModelEntity_Script_SetModelScale",
    "CBaseModelEntity_ScriptLookupAttachment",
    "CBaseModelEntity_ScriptGetAttachmentOrigin",
    "CBaseModelEntity_ScriptGetAttachmentAngles",
    "CBaseModelEntity_ScriptGetAttachmentForward",
    "CBaseModelEntity_ScriptSetSize",
    "CBaseModelEntity_ScriptSetModel",
    "CBaseModelEntity_ScriptGetRenderAlpha",
    "CBaseModelEntity_ScriptSetRenderAlpha",
    "CBaseModelEntity_ScriptSetRenderMode",
    "CBaseModelEntity_ScriptSetRenderColor",
    "CBaseModelEntity_ScriptGetRenderColor",
    "CBaseModelEntity_ScriptSetMaterialGroupHash",
    "CBaseModelEntity_ScriptGetMaterialGroupHash",
    "CBaseModelEntity_ScriptSetMeshGroupMask",
    "CBaseModelEntity_ScriptGetMeshGroupMask",
    "CBaseModelEntity_ScriptSetBodygroupByName",
    "CBaseModelEntity_Script_SetBodygroup",
    "CBaseModelEntity_Script_SetSkin",
]

LLM_DECOMPILE = [
    # (symbol_name, path_to_prompt, path_to_reference)
    (name, "prompt/call_llm_decompile.md",
     "references/server/CBaseModelEntity_GetScriptDescInternal.{platform}.yaml")
    for name in TARGET_FUNCTION_NAMES
]

GENERATE_YAML_DESIRED_FIELDS = [
    # (symbol_name, generate_yaml_fields)
    (
        name,
        [
            "func_name",
            "func_sig",
            "func_sig_allow_across_function_boundary:true",
            "func_va",
            "func_rva",
            "func_size",
        ],
    )
    for name in TARGET_FUNCTION_NAMES
]

async def preprocess_skill(
    session, skill_name, expected_outputs, old_yaml_map,
    new_binary_dir, platform, image_base, llm_config=None, debug=False,
):
    """Reuse previous gamever func_sig to locate target function(s) and write YAML."""
    return await preprocess_common_skill(
        session=session,
        expected_outputs=expected_outputs,
        old_yaml_map=old_yaml_map,
        new_binary_dir=new_binary_dir,
        platform=platform,
        image_base=image_base,
        func_names=TARGET_FUNCTION_NAMES,
        llm_decompile_specs=LLM_DECOMPILE,
        llm_config=llm_config,
        generate_yaml_desired_fields=GENERATE_YAML_DESIRED_FIELDS,
        debug=debug,
    )
