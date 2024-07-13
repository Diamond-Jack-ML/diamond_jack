WITH CommentRank AS (
  SELECT
    fc.page_id,
    fc.version_created_at AS comment_created,
    FORMAT(
      'Page Comment %d\nCreated On : %s\nTitle : %s\nStatus : %s\n%s\n%s\n%s\n',
      ROW_NUMBER() OVER(PARTITION BY fc.page_id ORDER BY fc.version_created_at),
      CAST(fc.version_created_at AS VARCHAR),
      fc.title,
      fc.status,
      '-------------------------',
      fcv.comment_body,
      '-------------------------'
    ) AS formatted_comment
  FROM
    footer_comment fc
  JOIN
    footer_comment_version fcv ON fc.id = fcv.comment_id
)
SELECT
  p.id as page_id,
  p.title as page_title,
  p.created_at as page_created,
  pv.page_body as page_content,
  FORMAT(
    '\nPage ID : %d\nCreated On : %s\nTitle : %s\n\n%s\n\n%s',
    p.id,
    CAST(p.created_at AS VARCHAR),
    p.title,
    pv.page_body,
    LISTAGG(cr.formatted_comment, '\n') WITHIN GROUP (ORDER BY cr.comment_created)
  ) AS page_details
FROM
  page p
JOIN
  page_version pv ON p.id = pv.page_id
LEFT JOIN
  CommentRank cr ON p.id = cr.page_id
GROUP BY
  p.id, p.title, p.created_at, pv.page_body;
