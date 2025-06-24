import { get } from './base'

export type BusinessLine = { id: string; name: string }

export const fetchBusinessLines = async () => {
  const res = await get<{ business_lines: BusinessLine[] }>('/business-lines')
  return res.business_lines
}
