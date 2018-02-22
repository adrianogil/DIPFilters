using System.Collections;
using System.Collections.Generic;
using UnityEngine;

#if UNITY_EDITOR
using UnityEditor;
#endif

public class TextureBlit : MonoBehaviour {

    public RenderTexture texture;
    public Material blitMaterial;

    private RenderTexture temp = null;

    [ContextMenu("Load RTX from Material")]
    public void LoadRTxFromMaterial()
    {
        Graphics.Blit(GetComponent<MeshRenderer>().sharedMaterial.mainTexture, texture);
    }

	// Use this for initialization
	void CreateTempRTx () {
        temp = new RenderTexture(texture.width, texture.height, 24);
	}

    public void Blit()
    {
        if (temp == null) {
            CreateTempRTx();
        }

        float[] w = new float [] {
            1f/9f,
            1f/9f,
            1f/9f,
            1f/9f,
            1f/9f,
            1f/9f,
            1f/9f,
            1f/9f,
            1f/9f,
        };
        Shader.SetGlobalFloatArray("_Kernel", w);
        Shader.SetGlobalFloat("_KernelLength", w.Length);

        // Graphics.Blit(texture, texture, blitMaterial) // Only on Mac?
        Graphics.Blit(texture, temp, blitMaterial);
        Graphics.Blit(temp, texture);
    }
}

#if UNITY_EDITOR
[CustomEditor(typeof(TextureBlit))]
public class TextureBlitEditor : Editor {

    public override void OnInspectorGUI()
    {
        base.OnInspectorGUI();

        TextureBlit editorObj = target as TextureBlit;

        if (editorObj == null) return;

        if (GUILayout.Button("Blit"))
        {
            editorObj.Blit();
        }
    }

}
#endif
