from graph import run_graph

def test_graph_pasta_dinner_requires_confirmation():
    state = run_graph()
    assert state['intent'] == 'meal_planning_cart_checkout'
    assert state['requires_confirmation'] is True
    assert any(item.get('agent') == 'checkout' for item in state['tool_results'])

