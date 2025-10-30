def is_full_bingo(card) -> bool:
    """Return True if every cell on the card is marked.

    We iterate the card's marked matrix directly instead of recomputing
    from the grid to avoid any mismatch and keep it O(rows*cols).
    """
    for r in range(card.rows):
        for c in range(card.cols):
            if not card.marked[r][c]:
                return False
    return True
