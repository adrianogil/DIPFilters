Shader "Custom/ConvFilter"
{
    Properties
    {
        _MainTex("Image", 2D) = "white"
    }
    Subshader
    {
        Pass
        {
            CGPROGRAM
            #pragma vertex vert
            #pragma fragment frag

            sampler _MainTex;
            float2 _MainTex_TexelSize;

            uniform int _KernelLength = 9;
            uniform float _Kernel[9];

            struct vert_input
            {
                float4 vertex : POSITION;
                float2 uv : TEXCOORD0;
            };

            struct vert_output
            {
                float4 vertex : SV_POSITION;
                float2 uv : TEXCOORD0;
            };

            vert_output vert(vert_input i)
            {
                vert_output o;

                o.vertex = UnityObjectToClipPos(i.vertex);
                o.uv = i.uv;

                return o;
            }

            half4 frag(vert_output o) : COLOR
            {
                float4 texColors[9];
                #define GRABPIXEL(px,py) tex2D( _MainTex, o.uv + float2(px * _MainTex_TexelSize.x, py * _MainTex_TexelSize.y))

                texColors[0] = _Kernel[0] * GRABPIXEL(-1,-1);
                texColors[1] = _Kernel[1] * GRABPIXEL(-1, 0);
                texColors[2] = _Kernel[2] * GRABPIXEL(-1, 1);
                texColors[3] = _Kernel[3] * GRABPIXEL( 0,-1);
                texColors[4] = _Kernel[4] * GRABPIXEL( 0, 0);
                texColors[5] = _Kernel[5] * GRABPIXEL( 0, 1);
                texColors[6] = _Kernel[6] * GRABPIXEL( 1,-1);
                texColors[7] = _Kernel[7] * GRABPIXEL( 1, 0);
                texColors[8] = _Kernel[8] * GRABPIXEL( 1, 1);

                return texColors[0] +
                        texColors[1] +
                        texColors[2] +
                        texColors[3] +
                        texColors[4] +
                        texColors[5] +
                        texColors[6] +
                        texColors[7] +
                        texColors[8];

            }

            ENDCG
        }
    }
}