# import requests
# import streamlit as st
# from typing import Any, Dict, List, Optional

# API_URL = "http://127.0.0.1:8000"

# st.set_page_config(
#     page_title="Multi-Agent Marketing Assistant",
#     page_icon="✨",
#     layout="wide",
#     initial_sidebar_state="expanded",
# )


# # ---------- Styling ----------
# def inject_css() -> None:
#     st.markdown(
#         """
#         <style>
#             .block-container {
#                 padding-top: 1.5rem;
#                 padding-bottom: 2rem;
#                 max-width: 1400px;
#             }

#             .hero {
#                 padding: 1.4rem 1.6rem;
#                 border-radius: 22px;
#                 background: linear-gradient(135deg, #121826 0%, #1f2a44 45%, #4f46e5 100%);
#                 color: white;
#                 margin-bottom: 1rem;
#                 box-shadow: 0 10px 30px rgba(0,0,0,0.12);
#             }

#             .hero h1 {
#                 font-size: 2rem;
#                 margin-bottom: 0.3rem;
#             }

#             .hero p {
#                 color: rgba(255,255,255,0.85);
#                 margin-bottom: 0;
#             }

#             .section-card {
#                 background: rgba(255,255,255,0.03);
#                 border: 1px solid rgba(120,120,120,0.18);
#                 padding: 1rem 1rem 0.8rem 1rem;
#                 border-radius: 18px;
#                 margin-bottom: 1rem;
#             }

#             .metric-card {
#                 border: 1px solid rgba(120,120,120,0.18);
#                 border-radius: 18px;
#                 padding: 1rem;
#                 background: rgba(255,255,255,0.02);
#                 min-height: 110px;
#             }

#             .pill {
#                 display: inline-block;
#                 padding: 0.25rem 0.65rem;
#                 border-radius: 999px;
#                 background: rgba(79, 70, 229, 0.12);
#                 border: 1px solid rgba(79, 70, 229, 0.28);
#                 margin-right: 0.45rem;
#                 margin-bottom: 0.35rem;
#                 font-size: 0.85rem;
#             }

#             .small-muted {
#                 font-size: 0.92rem;
#                 opacity: 0.75;
#             }

#             div[data-testid="stButton"] > button {
#                 border-radius: 12px;
#                 font-weight: 600;
#                 padding: 0.6rem 1rem;
#             }

#             div[data-testid="stTabs"] button {
#                 border-radius: 10px 10px 0 0;
#             }
#         </style>
#         """,
#         unsafe_allow_html=True,
#     )


# # ---------- API ----------
# def post_json(endpoint: str, payload: Dict[str, Any], timeout: int = 60) -> Dict[str, Any]:
#     response = requests.post(f"{API_URL}{endpoint}", json=payload, timeout=timeout)
#     response.raise_for_status()
#     return response.json()


# # ---------- Session State ----------
# def init_state() -> None:
#     defaults = {
#         "flow_result": None,
#         "weekly_plan": None,
#         "saved_inspiration_result": None,
#         "saved_brand_doc_result": None,
#     }
#     for key, value in defaults.items():
#         if key not in st.session_state:
#             st.session_state[key] = value


# # ---------- Reusable UI ----------
# def render_hero() -> None:
#     st.markdown(
#         """
#         <div class="hero">
#             <h1>Multi-Agent Marketing Assistant</h1>
#             <p>Strategy, content generation, review, planning, and retrieval-backed inspiration in one demo-ready interface.</p>
#         </div>
#         """,
#         unsafe_allow_html=True,
#     )


# def render_metric_cards() -> None:
#     col1, col2, col3, col4 = st.columns(4)
#     with col1:
#         st.markdown(
#             """
#             <div class="metric-card">
#                 <div class="small-muted">Agents</div>
#                 <h3>5</h3>
#                 <div class="small-muted">Strategy, Copywriter, Reviewer, Planner, Orchestrator</div>
#             </div>
#             """,
#             unsafe_allow_html=True,
#         )
#     with col2:
#         st.markdown(
#             """
#             <div class="metric-card">
#                 <div class="small-muted">Retrieval</div>
#                 <h3>Advanced RAG</h3>
#                 <div class="small-muted">Chunking, metadata, citations, inspiration ingestion</div>
#             </div>
#             """,
#             unsafe_allow_html=True,
#         )
#     with col3:
#         st.markdown(
#             """
#             <div class="metric-card">
#                 <div class="small-muted">Mode</div>
#                 <h3>Demo Ready</h3>
#                 <div class="small-muted">Product-style UX for interviews and LinkedIn showcases</div>
#             </div>
#             """,
#             unsafe_allow_html=True,
#         )
#     with col4:
#         st.markdown(
#             """
#             <div class="metric-card">
#                 <div class="small-muted">Backend</div>
#                 <h3>Connected</h3>
#                 <div class="small-muted">FastAPI endpoints preserved with minimal frontend-only abstraction</div>
#             </div>
#             """,
#             unsafe_allow_html=True,
#         )


# def render_sidebar() -> Dict[str, str]:
#     with st.sidebar:
#         st.markdown("## Workspace")
#         st.caption("Configure the marketing request and run flows.")

#         business_name = st.text_input("Business name", value="Sweet Cookies")
#         audience = st.text_input("Audience", value="young women")
#         platform = st.selectbox("Platform", ["Instagram", "Pinterest", "LinkedIn", "Facebook"])

#         st.divider()
#         st.markdown("### Demo tips")
#         st.markdown(
#             "- Start with the Dashboard\n"
#             "- Add inspiration sources\n"
#             "- Run the full flow\n"
#             "- Show citations and review loop\n"
#             "- Finish with the weekly plan"
#         )

#     return {
#         "business_name": business_name,
#         "audience": audience,
#         "platform": platform,
#     }


# def render_dashboard(inputs: Dict[str, str]) -> None:
#     st.markdown("## Dashboard")
#     left, right = st.columns([1.3, 1])

#     with left:
#         st.markdown('<div class="section-card">', unsafe_allow_html=True)
#         st.markdown("### Campaign Brief")
#         c1, c2 = st.columns(2)
#         c1.text_input("Business", value=inputs["business_name"], disabled=True)
#         c2.selectbox("Platform", [inputs["platform"]], disabled=True)
#         st.text_input("Target audience", value=inputs["audience"], disabled=True)
#         st.markdown("</div>", unsafe_allow_html=True)

#     with right:
#         st.markdown('<div class="section-card">', unsafe_allow_html=True)
#         st.markdown("### Flow Overview")
#         st.markdown(
#             "<span class='pill'>1. Strategy</span>"
#             "<span class='pill'>2. Copywriting</span>"
#             "<span class='pill'>3. Review</span>"
#             "<span class='pill'>4. Sources</span>"
#             "<span class='pill'>5. Weekly Planning</span>",
#             unsafe_allow_html=True,
#         )
#         st.caption("Use the pages below to demo ingestion, generation, and retrieved evidence.")
#         st.markdown("</div>", unsafe_allow_html=True)



# def render_inspiration_page(inputs: Dict[str, str]) -> None:
#     st.markdown("## Knowledge & Inspiration")
#     left, right = st.columns(2)

#     with left:
#         st.markdown('<div class="section-card">', unsafe_allow_html=True)
#         st.markdown("### Add Manual Inspiration")
#         insp_title = st.text_input("Inspiration title", value="cozy_instagram_style")
#         insp_content = st.text_area(
#             "Inspiration content",
#             value="Soft, cozy, feminine captions focused on emotional storytelling, gifting moments, warm colors, and lifestyle vibes.",
#             height=180,
#         )
#         insp_account = st.text_input("Account name", value="cozyvibesinspo")
#         insp_tags = st.text_input("Tags", value="cozy, feminine, storytelling")

#         if st.button("Save inspiration", use_container_width=True):
#             payload = {
#                 "title": insp_title,
#                 "content": insp_content,
#                 "platform": inputs["platform"],
#                 "account_name": insp_account,
#                 "content_type": "inspiration_post",
#                 "tags": [tag.strip() for tag in insp_tags.split(",") if tag.strip()],
#             }
#             try:
#                 st.session_state["saved_inspiration_result"] = post_json(
#                     "/ingest-manual-inspiration", payload, timeout=60
#                 )
#                 st.success("Inspiration saved successfully.")
#             except Exception as e:
#                 st.error(f"Failed to save inspiration: {e}")

#         if st.session_state["saved_inspiration_result"]:
#             with st.expander("Saved inspiration response", expanded=False):
#                 st.json(st.session_state["saved_inspiration_result"])
#         st.markdown("</div>", unsafe_allow_html=True)

#     with right:
#         st.markdown('<div class="section-card">', unsafe_allow_html=True)
#         st.markdown("### Add Brand Document")
#         doc_title = st.text_input("Brand doc title", value="brand_doc_1")
#         doc_content = st.text_area(
#             "Brand doc content",
#             value="Sweet Cookies is a handmade premium dessert brand focused on emotional storytelling, gifting moments, and cozy lifestyle branding for young women.",
#             height=180,
#         )
#         doc_account = st.text_input("Brand account name", value="sweetcookies")
#         doc_tags = st.text_input("Brand tags", value="desserts, cozy, gifting")

#         if st.button("Save brand doc", use_container_width=True):
#             payload = {
#                 "filename": doc_title,
#                 "content": doc_content,
#                 "source": "manual_upload",
#                 "source_type": "brand_doc",
#                 "platform": inputs["platform"],
#                 "account_name": doc_account,
#                 "content_type": "brand_guide",
#                 "tags": [tag.strip() for tag in doc_tags.split(",") if tag.strip()],
#             }
#             try:
#                 st.session_state["saved_brand_doc_result"] = post_json("/upload-doc", payload, timeout=60)
#                 st.success("Brand document saved successfully.")
#             except Exception as e:
#                 st.error(f"Failed to save brand document: {e}")

#         if st.session_state["saved_brand_doc_result"]:
#             with st.expander("Saved brand document response", expanded=False):
#                 st.json(st.session_state["saved_brand_doc_result"])
#         st.markdown("</div>", unsafe_allow_html=True)



# def render_generation_page(inputs: Dict[str, str]) -> None:
#     st.markdown("## Content Studio")

#     action_col, helper_col = st.columns([1.2, 0.8])
#     with action_col:
#         if st.button("Generate Full Marketing Flow", type="primary", use_container_width=True):
#             payload = {
#                 "business_name": inputs["business_name"],
#                 "audience": inputs["audience"],
#                 "platform": inputs["platform"],
#             }
#             try:
#                 with st.spinner("Running multi-agent workflow..."):
#                     st.session_state["flow_result"] = post_json(
#                         "/run-marketing-flow", payload, timeout=120
#                     )
#                 st.success("Workflow completed.")
#             except Exception as e:
#                 st.error(f"Workflow failed: {e}")

#     with helper_col:
#         st.info("Run this during your demo to show the full agent chain: strategy → generation → review → evidence.")

#     result = st.session_state.get("flow_result")
#     if not result:
#         st.warning("No generated result yet. Run the full marketing flow to populate this page.")
#         return

#     tab1, tab2, tab3, tab4 = st.tabs(["Strategy", "Content", "Review", "Sources"])

#     with tab1:
#         strategy = result.get("strategy", {})
#         st.markdown('<div class="section-card">', unsafe_allow_html=True)
#         st.markdown("### Strategy Output")
#         if isinstance(strategy, dict):
#             cols = st.columns(2)
#             with cols[0]:
#                 st.write(f"**Business:** {strategy.get('business_name', inputs['business_name'])}")
#                 st.write(f"**Tone:** {strategy.get('tone', '—')}")
#                 st.write(f"**Campaign Idea:** {strategy.get('campaign_idea', '—')}")
#             with cols[1]:
#                 st.write(f"**Agent:** {strategy.get('agent', '—')}")
#                 pillars = strategy.get("pillars", [])
#                 if pillars:
#                     st.write("**Content Pillars:**")
#                     for pillar in pillars:
#                         st.markdown(f"- {pillar}")
#             with st.expander("Raw strategy JSON"):
#                 st.json(strategy)
#         else:
#             st.json(strategy)
#         st.markdown("</div>", unsafe_allow_html=True)

#     with tab2:
#         content = result.get("content", {})
#         st.markdown('<div class="section-card">', unsafe_allow_html=True)
#         st.markdown("### Generated Content")
#         st.text_area(
#             "Final marketing copy",
#             value=content.get("content", ""),
#             height=260,
#             label_visibility="collapsed",
#         )
#         meta1, meta2 = st.columns(2)
#         meta1.caption(f"Generated by: {content.get('agent', '—')}")
#         meta2.caption(f"Platform: {content.get('platform', inputs['platform'])}")
#         st.markdown("</div>", unsafe_allow_html=True)

#     with tab3:
#         review = result.get("review", {})
#         st.markdown('<div class="section-card">', unsafe_allow_html=True)
#         st.markdown("### Review & Improvement")
#         st.json(review)
#         st.markdown("</div>", unsafe_allow_html=True)

#     with tab4:
#         sources = result.get("sources", [])
#         st.markdown("### Retrieved Sources")
#         if not sources:
#             st.info("No sources returned.")
#         for idx, source in enumerate(sources, start=1):
#             with st.container(border=True):
#                 title_col, meta_col = st.columns([1.4, 1])
#                 with title_col:
#                     st.markdown(f"**Source {idx}: {source.get('title', 'Untitled')}**")
#                     st.caption(source.get("text", "")[:180] + ("..." if len(source.get("text", "")) > 180 else ""))
#                 with meta_col:
#                     st.caption(f"Chunk ID: {source.get('chunk_id', '—')}")
#                     st.caption(f"Source: {source.get('source', '—')}")
#                     st.caption(f"Type: {source.get('source_type', '—')}")
#                     if source.get("platform"):
#                         st.caption(f"Platform: {source.get('platform')}")
#                     if source.get("account_name"):
#                         st.caption(f"Account: {source.get('account_name')}")

#                 st.text_area(
#                     f"Snippet {idx}",
#                     value=source.get("text", ""),
#                     height=130,
#                     key=f"source_text_{idx}",
#                 )



# def render_planner_page(inputs: Dict[str, str]) -> None:
#     st.markdown("## Weekly Planner")
#     st.caption("Generate a weekly content plan using the existing backend planner.")

#     if st.button("Generate Weekly Plan", use_container_width=True):
#         payload = {
#             "business_name": inputs["business_name"],
#             "audience": inputs["audience"],
#             "platform": inputs["platform"],
#         }
#         try:
#             with st.spinner("Generating weekly plan..."):
#                 st.session_state["weekly_plan"] = post_json(
#                     "/generate-weekly-plan", payload, timeout=60
#                 )
#             st.success("Weekly plan generated.")
#         except Exception as e:
#             st.error(f"Failed to generate weekly plan: {e}")

#     result = st.session_state.get("weekly_plan")
#     if result:
#         st.markdown('<div class="section-card">', unsafe_allow_html=True)
#         st.markdown("### Weekly Plan Output")
#         st.json(result)
#         st.markdown("</div>", unsafe_allow_html=True)
#     else:
#         st.info("No weekly plan generated yet.")



# def main() -> None:
#     inject_css()
#     init_state()
#     render_hero()
#     render_metric_cards()
#     inputs = render_sidebar()

#     pages = {
#         "Dashboard": render_dashboard,
#         "Knowledge & Inspiration": render_inspiration_page,
#         "Content Studio": render_generation_page,
#         "Weekly Planner": render_planner_page,
#     }

#     selected_page = st.segmented_control(
#         "Navigate",
#         options=list(pages.keys()),
#         default="Dashboard",
#         key="page_selector",
#     )

#     pages[selected_page](inputs)


# if __name__ == "__main__":
#     main()


import requests
import streamlit as st
from typing import Any, Dict, List

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Multi-Agent Marketing Assistant",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded",
)


# =========================
# CSS
# =========================
def inject_css() -> None:
    st.markdown(
        """
        <style>
        .block-container {
            padding-top: 1.5rem;
            max-width: 1250px;
        }

        .hero {
            padding: 30px 34px;
            border-radius: 26px;
            background: linear-gradient(135deg, #f7f8ff 0%, #eef2ff 100%);
            border: 1px solid #e0e7ff;
            margin-bottom: 24px;
        }

        .hero h1 {
            color: #111827;
            font-size: 2.25rem;
            margin-bottom: 0.35rem;
        }

        .hero p {
            color: #6b7280;
            font-size: 1.02rem;
            margin-bottom: 0;
        }

        .soft-card {
            padding: 18px 20px;
            border-radius: 18px;
            border: 1px solid #e5e7eb;
            background: #ffffff;
            box-shadow: 0 8px 24px rgba(15, 23, 42, 0.05);
            margin-bottom: 16px;
        }

        .agent-step {
            padding: 12px 14px;
            border-radius: 14px;
            border: 1px solid #e5e7eb;
            background: #ffffff;
            margin-bottom: 8px;
            font-weight: 600;
        }

        .score-box {
            padding: 18px;
            border-radius: 18px;
            background: #f9fafb;
            border: 1px solid #e5e7eb;
            text-align: center;
        }

        .score-number {
            font-size: 2rem;
            font-weight: 800;
            color: #4338ca;
        }

        .approved {
            display: inline-block;
            padding: 6px 12px;
            border-radius: 999px;
            background: #dcfce7;
            color: #166534;
            font-weight: 700;
            font-size: 0.86rem;
        }

        .not-approved {
            display: inline-block;
            padding: 6px 12px;
            border-radius: 999px;
            background: #fee2e2;
            color: #991b1b;
            font-weight: 700;
            font-size: 0.86rem;
        }

        div[data-testid="stButton"] > button {
            border-radius: 12px;
            font-weight: 700;
            padding: 0.65rem 1rem;
        }

        textarea {
            border-radius: 14px !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


# =========================
# API HELPERS
# =========================
def post_json(endpoint: str, payload: Dict[str, Any], timeout: int = 90) -> Dict[str, Any]:
    response = requests.post(f"{API_URL}{endpoint}", json=payload, timeout=timeout)
    response.raise_for_status()
    return response.json()


# =========================
# STATE
# =========================
def init_state() -> None:
    defaults = {
        "user_result": None,
        "developer_result": None,
        "developer_payload": None,
        "weekly_plan": None,
        "saved_inspiration_result": None,
        "saved_brand_doc_result": None,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


# =========================
# UI HELPERS
# =========================
def render_hero(title: str, subtitle: str) -> None:
    st.markdown(
        f"""
        <div class="hero">
            <h1>{title}</h1>
            <p>{subtitle}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_agent_flow() -> None:
    st.markdown("### Agent workflow")
    steps = [
        "✅ Strategy Agent — creates campaign direction",
        "✅ RAG Retriever — loads brand and inspiration context",
        "✅ Copywriter Agent — generates platform-ready content",
        "✅ Reviewer Agent — scores and suggests improvements",
        "✅ Source Tracing — returns the retrieved chunks",
    ]
    for step in steps:
        st.markdown(f'<div class="agent-step">{step}</div>', unsafe_allow_html=True)


def render_review(review: Dict[str, Any]) -> None:
    score = review.get("score", "—")
    approved = review.get("approved", False)
    strengths = review.get("strengths", [])
    improvements = review.get("improvements", [])

    col1, col2 = st.columns([0.35, 0.65])

    with col1:
        st.markdown(
            f"""
            <div class="score-box">
                <div class="score-number">{score}/10</div>
                <div class="{'approved' if approved else 'not-approved'}">
                    {'Approved' if approved else 'Needs Improvement'}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown("**Strengths**")
        for item in strengths:
            st.markdown(f"- {item}")

        st.markdown("**Improvements**")
        for item in improvements:
            st.markdown(f"- {item}")


def render_sources(sources: List[Dict[str, Any]]) -> None:
    if not sources:
        st.info("No sources returned.")
        return

    for idx, source in enumerate(sources, start=1):
        with st.container(border=True):
            st.markdown(f"**Source {idx}: {source.get('title', 'Untitled')}**")
            st.caption(f"Chunk ID: {source.get('chunk_id', '—')}")
            st.caption(
                f"Source: {source.get('source', '—')} | "
                f"Type: {source.get('source_type', '—')}"
            )

            if source.get("platform"):
                st.caption(f"Platform: {source.get('platform')}")

            if source.get("account_name"):
                st.caption(f"Account: {source.get('account_name')}")

            st.text_area(
                f"Snippet {idx}",
                value=source.get("text", ""),
                height=110,
                key=f"source_{idx}_{source.get('chunk_id', idx)}",
            )


# =========================
# USER MODE
# =========================
def render_user_mode() -> None:
    render_hero(
        "✨ AI Marketing Assistant",
        "Create strategy-aware marketing content using multiple AI agents and brand context.",
    )

    st.markdown("## Create content")

    with st.container(border=True):
        col1, col2 = st.columns(2)

        with col1:
            business = st.selectbox(
                "Brand / Field",
                ["Bakery", "Fitness", "Fashion", "Tech", "Education", "Beauty", "Other"],
            )

            if business == "Other":
                business = st.text_input(
                    "Add your field",
                    placeholder="Example: AI startup, coffee shop, handmade jewelry",
                )

            audience = st.selectbox(
                "Target audience",
                [
                    "Young women",
                    "Students",
                    "Professionals",
                    "Families",
                    "Small business owners",
                    "Tech professionals",
                    "Other",
                ],
            )

            if audience == "Other":
                audience = st.text_input(
                    "Add your audience",
                    placeholder="Example: students looking for internships",
                )

            platform = st.selectbox(
                "Platform",
                ["Instagram", "LinkedIn", "TikTok", "Pinterest", "Facebook"],
            )

        with col2:
            concept_options = {
                "Bakery": [
                    "Gift moments",
                    "New product launch",
                    "Behind the scenes",
                    "Seasonal offer",
                    "Customer story",
                    "Other",
                ],
                "Fitness": [
                    "Workout motivation",
                    "Healthy lifestyle",
                    "Beginner tips",
                    "Transformation story",
                    "Program promotion",
                    "Other",
                ],
                "Fashion": [
                    "Outfit inspiration",
                    "New collection",
                    "Styling tips",
                    "Personal brand",
                    "Seasonal trends",
                    "Other",
                ],
                "Tech": [
                    "Career tips",
                    "AI tools",
                    "Internship advice",
                    "Learning roadmap",
                    "Portfolio project",
                    "Product launch",
                    "Other",
                ],
                "Education": [
                    "Learning tips",
                    "Course promotion",
                    "Student success story",
                    "Study roadmap",
                    "Career guidance",
                    "Other",
                ],
                "Beauty": [
                    "Product routine",
                    "Before and after",
                    "Self-care tips",
                    "New product launch",
                    "Customer testimonial",
                    "Other",
                ],
            }

            concept = st.selectbox(
                "Content topic",
                concept_options.get(
                    business,
                    ["Brand awareness", "Product launch", "Educational post", "Other"],
                ),
            )

            if concept == "Other":
                concept = st.text_input(
                    "Add your content topic",
                    placeholder="Example: how students can build their first AI portfolio",
                )

            style = st.selectbox(
                "Content style",
                [
                    "Professional",
                    "Emotional storytelling",
                    "Luxury",
                    "Fun & playful",
                    "Minimal & clean",
                    "Educational",
                    "Viral",
                ],
            )

            goal = st.selectbox(
                "Content goal",
                [
                    "Increase awareness",
                    "Educate audience",
                    "Promote a product",
                    "Build trust",
                    "Drive engagement",
                    "Attract leads",
                ],
            )

    business_context = f"""
Brand / Field: {business}
Target audience: {audience}
Platform: {platform}
Content topic: {concept}
Content style: {style}
Content goal: {goal}

Important:
Generate content that matches this exact scenario.
Do not use examples from unrelated businesses.
""".strip()

    if st.button("✨ Generate Marketing Content", type="primary", use_container_width=True):
        payload = {
            "business_name": business_context,
            "audience": audience,
            "platform": platform,
        }

        try:
            with st.spinner("Running Strategy → RAG → Copywriter → Reviewer..."):
                st.session_state["user_result"] = post_json(
                    "/run-marketing-flow",
                    payload,
                    timeout=140,
                )
            st.success("Marketing flow completed.")
        except Exception as e:
            st.error(f"Backend error: {e}")
            st.info("Make sure FastAPI is running on http://127.0.0.1:8000")

    result = st.session_state.get("user_result")

    if result:
        st.divider()
        st.markdown("## Result")

        content = result.get("content", {}).get("content", "")
        review = result.get("review", {})
        strategy = result.get("strategy", {})
        sources = result.get("sources", [])

        top_left, top_right = st.columns([1.5, 1])

        with top_left:
            st.markdown("### Generated post")
            st.text_area(
                "Generated content",
                value=content,
                height=260,
                label_visibility="collapsed",
            )

        with top_right:
            render_agent_flow()

        tab1, tab2, tab3 = st.tabs(["Strategy", "Review", "Sources"])

        with tab1:
            st.markdown("### Strategy")
            if strategy.get("tone"):
                st.write(f"**Tone:** {strategy.get('tone')}")
            if strategy.get("campaign_idea"):
                st.write(f"**Campaign idea:** {strategy.get('campaign_idea')}")
            if strategy.get("pillars"):
                st.write("**Content pillars:**")
                for pillar in strategy.get("pillars", []):
                    st.markdown(f"- {pillar}")

        with tab2:
            st.markdown("### AI Review")
            render_review(review)

        with tab3:
            st.markdown("### Retrieved Sources")
            render_sources(sources)


# =========================
# DEVELOPER MODE
# =========================
def render_developer_mode() -> None:
    render_hero(
        "🛠 Developer Mode",
        "Technical view for payloads, agents, RAG sources, backend responses, and debugging.",
    )

    st.markdown("## Technical request")

    col1, col2, col3 = st.columns(3)

    with col1:
        business_name = st.text_input("Business name", value="Sweet Cookies")

    with col2:
        audience = st.text_input("Audience", value="young women")

    with col3:
        platform = st.selectbox(
            "Platform",
            ["Instagram", "Pinterest", "LinkedIn", "Facebook"],
        )

    st.divider()

    with st.expander("Add manual inspiration"):
        insp_title = st.text_input("Inspiration title", value="cozy_instagram_style")
        insp_content = st.text_area(
            "Inspiration content",
            value="Soft, cozy, feminine captions focused on emotional storytelling, gifting moments, warm colors, and lifestyle vibes.",
            height=140,
        )
        insp_account = st.text_input("Account name", value="cozyvibesinspo")
        insp_tags = st.text_input("Tags", value="cozy, feminine, storytelling")

        if st.button("Save inspiration", use_container_width=True):
            payload = {
                "title": insp_title,
                "content": insp_content,
                "platform": platform,
                "account_name": insp_account,
                "content_type": "inspiration_post",
                "tags": [tag.strip() for tag in insp_tags.split(",") if tag.strip()],
            }

            try:
                st.session_state["saved_inspiration_result"] = post_json(
                    "/ingest-manual-inspiration",
                    payload,
                    timeout=60,
                )
                st.success("Inspiration saved successfully.")
                st.json(st.session_state["saved_inspiration_result"])
            except Exception as e:
                st.error(f"Failed to save inspiration: {e}")

    with st.expander("Add brand document"):
        doc_title = st.text_input("Brand doc title", value="brand_doc_1")
        doc_content = st.text_area(
            "Brand doc content",
            value="Sweet Cookies is a handmade premium dessert brand focused on emotional storytelling, gifting moments, and cozy lifestyle branding for young women.",
            height=140,
        )
        doc_account = st.text_input("Brand account name", value="sweetcookies")
        doc_tags = st.text_input("Brand tags", value="desserts, cozy, gifting")

        if st.button("Save brand doc", use_container_width=True):
            payload = {
                "filename": doc_title,
                "content": doc_content,
                "source": "manual_upload",
                "source_type": "brand_doc",
                "platform": platform,
                "account_name": doc_account,
                "content_type": "brand_guide",
                "tags": [tag.strip() for tag in doc_tags.split(",") if tag.strip()],
            }

            try:
                st.session_state["saved_brand_doc_result"] = post_json(
                    "/upload-doc",
                    payload,
                    timeout=60,
                )
                st.success("Brand document saved successfully.")
                st.json(st.session_state["saved_brand_doc_result"])
            except Exception as e:
                st.error(f"Failed to save brand document: {e}")

    st.divider()

    if st.button("Run Full Marketing Flow", type="primary", use_container_width=True):
        payload = {
            "business_name": business_name,
            "audience": audience,
            "platform": platform,
        }

        try:
            with st.spinner("Running multi-agent workflow..."):
                st.session_state["developer_result"] = post_json(
                    "/run-marketing-flow",
                    payload,
                    timeout=140,
                )
                st.session_state["developer_payload"] = payload
            st.success("Workflow completed.")
        except Exception as e:
            st.error(f"Workflow failed: {e}")

    result = st.session_state.get("developer_result")
    payload = st.session_state.get("developer_payload")

    if result:
        tab1, tab2, tab3, tab4, tab5 = st.tabs(
            ["Payload", "Strategy", "Content", "Review", "Sources"]
        )

        with tab1:
            st.json(payload)

        with tab2:
            st.json(result.get("strategy", {}))

        with tab3:
            st.text_area(
                "Generated content",
                value=result.get("content", {}).get("content", ""),
                height=260,
            )
            st.json(result.get("content", {}))

        with tab4:
            render_review(result.get("review", {}))
            st.json(result.get("review", {}))

        with tab5:
            render_sources(result.get("sources", []))

    st.divider()
    st.markdown("## Weekly Planner")

    if st.button("Generate Weekly Plan", use_container_width=True):
        payload = {
            "business_name": business_name,
            "audience": audience,
            "platform": platform,
        }

        try:
            with st.spinner("Generating weekly plan..."):
                st.session_state["weekly_plan"] = post_json(
                    "/generate-weekly-plan",
                    payload,
                    timeout=60,
                )
            st.success("Weekly plan generated.")
        except Exception as e:
            st.error(f"Failed to generate weekly plan: {e}")

    if st.session_state.get("weekly_plan"):
        st.json(st.session_state["weekly_plan"])


# =========================
# MAIN
# =========================
def main() -> None:
    inject_css()
    init_state()

    mode = st.sidebar.radio(
        "View mode",
        ["✨ User Mode", "🛠 Developer Mode"],
    )

    st.sidebar.divider()
    st.sidebar.caption("User Mode: simple product experience")
    st.sidebar.caption("Developer Mode: technical system visibility")
    st.sidebar.divider()
    st.sidebar.caption("Backend: FastAPI")
    st.sidebar.caption("Agents: Strategy, Copywriter, Reviewer, Planner")
    st.sidebar.caption("RAG: Brand docs + inspiration sources")

    if mode == "✨ User Mode":
        render_user_mode()
    else:
        render_developer_mode()


if __name__ == "__main__":
    main()
